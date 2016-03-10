#!/usr/bin/python
# Given a BST, determine if it is balanced, where balanced means height
# +/- 1 on any subtree
import unittest
from tree import *

def balanced(head):
    if not head:
        return 0

    leftHeight = balanced(head.left)
    rightHeight = balanced(head.right)

    if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
        return -1

    return 1 + max(leftHeight, rightHeight)

def helper(t):
    printTree(t)
    return balanced(deserialize(t)) > 0

class TestClass(unittest.TestCase):
    def test_1(self):
        a = '{16,8,32,4,12,20,#,#,#,#,#,15,17}'
        self.assertFalse(helper(a))

    def test_2(self):
        a = '{1,2,3}'
        self.assertTrue(helper(a))

    def test_3(self):
        a = '{1,2,3,4,5,#,#,6}'
        self.assertFalse(helper(a))

unittest.main()
