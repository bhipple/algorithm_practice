#!/usr/bin/python
# Given a sorted linked list, convert it to a balanced binary search tree
import unittest

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def printList(head):
    if head:
        print head.val
        printList(head.next)

def printTree(head):
    if not head:
        return
    printTree(head.left)
    print head.val
    printTree(head.right)

class TestClass(unittest.TestCase):
    def setUp(self):
        self.a = ListNode(5)
        self.b = ListNode(12)
        self.c = ListNode(26)
        self.d = ListNode(54)
        self.e = ListNode(110)
        self.f = ListNode(222)
        self.a.next = self.b
        self.b.next = self.c
        self.c.next = self.d
        self.d.next = self.e
        self.e.next = self.f

    def test_ex(self):
        printList(self.a)

unittest.main()
