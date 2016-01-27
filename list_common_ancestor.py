#!/usr/bin/python
# Given two lists that converge at some point, find their common ancestor
import unittest

class Node:
    def __init__(self, val, nxt = None):
        self.val = val
        self.next = nxt

def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def solution(a, b):
    aLen = length(a)
    bLen = length(b)
    while aLen > bLen:
        a = a.next
        aLen -= 1
    while bLen > aLen:
        b = b.next
        bLen -= 1

    while a != b:
        a = a.next
        b = b.next

    return a

class TestClass(unittest.TestCase):
    def setUp(self):
        self.d = Node(5)
        self.c = Node(4, self.d) # Common ancestor

        self.b1 = Node(3, self.c)
        self.a1 = Node(2, self.c)
        self.a2 = Node(1, self.a1)

    def test_simple(self):
        res = solution(self.a2, self.b1)
        self.assertEqual(res, self.c)

    def test_simple2(self):
        res = solution(self.b1, self.a2)
        self.assertEqual(res, self.c)

    def test_same(self):
        res = solution(self.c, self.c)
        self.assertEqual(res, self.c)

    def test_oneAtAncestor(self):
        res = solution(self.c, self.a2)
        self.assertEqual(res, self.c)


unittest.main()
