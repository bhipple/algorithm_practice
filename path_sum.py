#!/usr/bin/python
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path
# such that adding up all the values along the path equals the given sum.

class TreeNode():
    def __init__(self, x):
        self.d = x
        self.left = None
        self.right = None

def pathSums(head):
    if not head:
        return []
    if not head.left and not head.right:
        return [head.d]
    leftSums = pathSums(head.left)
    rightSums = pathSums(head.right)

    print head.d, "\t", leftSums, "\t\t", rightSums
    return [head.d + x for x in leftSums + rightSums]

def pathSum(tree, x):
    paths = pathSums(tree)
    valid = filter(lambda y: y == x, paths)
    return len(valid) > 0


a = TreeNode(16)
a.left = TreeNode(8)
a.right = TreeNode(32)
a.left.left = TreeNode(4)
a.left.right = TreeNode(12)
a.right.left = TreeNode(20)
a.right.left.left = TreeNode(15)
a.right.left.right = TreeNode(17)

print pathSums(a)
