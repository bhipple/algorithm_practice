#!/usr/bin/python
# Given a BST and a range [x,y], return all elements in the range
import unittest

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def inRange(head, x, y):
    if not head:
        return []
    if head.val < x:
        return inRange(head.right, x, y)
    if head.val > y:
        return inRange(head.left, x, y)

    return inRange(head.left, x, y) + [head.val] + inRange(head.right, x, y)

class TestClass(unittest.TestCase):
    def setUp(self):
        self.a = TreeNode(16)
        self.b = TreeNode(8)
        self.c = TreeNode(32)
        self.d = TreeNode(12)
        self.e = TreeNode(9)

        self.a.left = self.b
        self.a.right = self.c

        self.b.right = self.d
        self.d.left = self.e

    def test_sol(self):
        self.assertEqual([], inRange(self.a, 33, 35))
        self.assertEqual([8,9], inRange(self.a, 0, 11))
        self.assertEqual([8,9], inRange(self.a, 0, 9))
        self.assertEqual([12,16], inRange(self.a, 12, 21))
        self.assertEqual([12,16,32], inRange(self.a, 12, 32))
        self.assertEqual([8,9,12,16,32], inRange(self.a, 0, 99))

unittest.main()
