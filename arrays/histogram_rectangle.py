#!/usr/bin/python
# Given a histogram, find the largest rectangle
# Input histogram is an integer array where each integer is the height
# of the bar of unit width at that x coordinate.
import unittest

def remove(hist, i, stack):
    top = stack.pop(0)
    if not len(stack):
        return hist[top] * i
    else:
        return hist[top] * (i - stack[0] - 1)

# Stack based approach
# O(2*n) = O(n) time complexity
# O(n) space complexity
def largestRectangle(hist):
    # For all i in range,
    # 1) Add to stack if current value is equal or bigger than top of stack
    # 2) Otherwise, keep removing from stack till a number which is <= current
    #    is found.
    #   2a) When removing, if stack is empty, area = input[top] * i
    #   2b) Otherwise, area = input[top] * (i - stack[0] - 1)
    maxArea = 0
    stack = []
    i = 0
    while i < len(hist):
        # This bar is >= top of stack (or stack is empty), so push it on
        if not len(stack) or hist[stack[0]] <= hist[i]:
            stack.insert(0, i)
            i += 1
        else:
            # This bar is smaller. Have to unwind to see what areas we can get
            maxArea = max(maxArea, remove(hist, i, stack))

    # Unwind anything left
    while len(stack):
        maxArea = max(maxArea, remove(hist, i, stack))

    return maxArea

class TestClass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(4, largestRectangle([1,2,4]))

    def test_2(self):
        self.assertEqual(5, largestRectangle([2,1,2,3,1]))

    def test_3(self):
        self.assertEqual(3, largestRectangle([2,1,2]))

    def test_4(self):
        self.assertEqual(3, largestRectangle([0,3,1,0]))

    def test_5(self):
        self.assertEqual(12, largestRectangle([6,2,5,4,5,1,6]))

unittest.main()
