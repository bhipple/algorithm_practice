#!/usr/bin/python
# Given a singly linked list, group all odd indexed nodes together followed by
# even indexed nodes. The first element is considered odd.
import unittest

class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def oddEvenList(head):
    if not head:
        return None

    lastOdd, cur = head, head.next
    while cur and cur.next:
        firstEven = lastOdd.next
        lastOdd.next = cur.next

        lastOdd = lastOdd.next
        cur.next = lastOdd.next
        lastOdd.next = firstEven

        cur = cur.next
    return head

def flatten(head):
    if not head:
        return []
    return [head.val] + flatten(head.next)

class Test(unittest.TestCase):
    def test_simple(self):
        a = Node(1)
        b = Node(2)
        c = Node(3)
        d = Node(4)
        e = Node(5)
        f = Node(6)
        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual([1,3,5,2,4,6], flatten(oddEvenList(a)))

if __name__ == "__main__":
    unittest.main()
