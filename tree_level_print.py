#!/usr/bin/python
# Write a function that takes a Tree and a level, and
# returns all node values at that level of the tree
import unittest
class Node():
    def __init__(self, val, children=[]):
        self.val = val
        self.children = children

def getLevel(head, level):
    if not head:
        return []
    if level == 1:
        return [head.val]
    return reduce(lambda acc, c: acc + getLevel(c, level-1),
                  head.children, [])

    # The above could also be written as:
    # res = []
    # for c in head.children:
    #    res += getLevel(c, level - 1)
    # return res

'''
            a
      b     c     d
     e f        g h i


'''
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
a.children = [b, c, d]
b.children = [e, f]
d.children = [g, h, i]

class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(['a'], getLevel(a, 1))

    def test_2(self):
        self.assertEqual(['b', 'c', 'd'], getLevel(a, 2))

    def test_3(self):
        self.assertEqual(['e', 'f', 'g', 'h', 'i'], getLevel(a, 3))

unittest.main()
