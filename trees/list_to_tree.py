#!/usr/bin/python
# Given a sorted linked list, convert it to a balanced binary search tree
import unittest
global lstHead

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

def preOrder(head):
    if not head:
        return
    print head.val
    preOrder(head.left)
    preOrder(head.right)

def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

# Wrapper to setup global and n
def solution(head):
    global lstHead
    lstHead = head
    return buildBst(length(lstHead))

def buildBst(n):
    global lstHead
    if n <= 0:
        return None

    # Left Subtree
    left = buildBst(n/2)

    # This subtree's root node
    root = TreeNode(lstHead.val)
    root.left = left
    #print "Added root %s" % root.val
    lstHead = lstHead.next

    # Right subtree
    root.right = buildBst(n - n/2 - 1)

    return root

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

    def test_solution(self):
        print "Starting list: "
        printList(self.a)

        print "Final Tree pre-order traversal:"
        preOrder(solution(self.a))

    def test_len(self):
        self.assertEqual(6, length(self.a))

unittest.main()
