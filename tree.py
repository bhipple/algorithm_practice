#!/usr/bin/python
# Helpers for Tree Questions
import drawtree  # pip install drawtree

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

def printTree(s):
    print "\nGiven this tree:"
    drawtree.draw_level_order(s)
    print ""
