#!/usr/bin/python
# Find the length of the longest path between two leaves of a tree, known as the
# "diameter" of a tree. This path may or may not go through the root.
import unittest
import drawtree  # pip install drawtree

## ============================================================================
## Helpers
## ============================================================================
class TreeNode(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Yanked from the the drawtree module (private function)
def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == '#' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root


## ============================================================================
## Solution
## ============================================================================
def diameter(head):
    if not head:
        return [0, 0]

    [longestLeft, f1] = diameter(head.left)
    [longestRight, f2] = diameter(head.right)

    # The best path that can be continued
    extensible = 1 + max(longestLeft, longestRight)

    # The best "finished" path
    finished = max([f1, f2, 1 + longestLeft + longestRight])

    return [extensible, finished]

def solution(head):
    return max(diameter(head))

def helper(s):
    print "Given this tree:"
    drawtree.draw_level_order(s)
    d = solution(deserialize(s))
    print "\nThe diameter is %s" % d
    return d

class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(6, helper('{16,8,32,4,12,20,#,#,#,#,#,15,17}'))

    def test_2(self):
        self.assertEqual(4, helper('{1,2,3,4,5,#,#}'))

    def test_NoRoot1(self):
        self.assertEqual(9, helper('{1,2,2,3,3,#,3,4,4,#,4,#,#,#,#,5,#,5,5,6,6,#,#,#,6}'))

    def test_NoRoot2(self):
        self.assertEqual(5, helper('{1,2,#,4,5,6,7,8}'))

unittest.main()
