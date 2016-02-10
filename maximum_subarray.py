#!/usr/bin/python
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Given a list, find the largest sum of a contiguous subarray.
import unittest

# Kadane's algorithm, just returning the value of the sum
def maxSubarraySum(arr):
    best = 0
    current = 0
    for i in range(len(arr)):
        current = max(current + arr[i], 0)
        best = max(best, current)
    return best

# Kadane's algorithm, returning the subarray
def maxSubarray(arr):
    best = 0
    bestStart = 0
    bestEnd = 0
    curVal = 0
    rurStart = 0
    curEnd = 0
    for i in range(len(arr)):
        curVal += arr[i]
        if curVal < 0:
            curVal = 0
            curStart = i+1
        curEnd = i
        if curVal > best:
            best = curVal
            bestStart = curStart
            bestEnd = curEnd

    return arr[bestStart:bestEnd+1]

class TestClass(unittest.TestCase):
    def test_name(self):
        a1 = maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual([4, -1, 2, 1], a1)

        a2 = maxSubarraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
        self.assertEqual(6, a2)

        a3 = maxSubarray([-2, 5, -1, 7, -3])
        self.assertEqual([5,-1,7], a3)

        a4 = maxSubarraySum([-2, 5, -1, 7, -3])
        self.assertEqual(11, a4)

unittest.main()
