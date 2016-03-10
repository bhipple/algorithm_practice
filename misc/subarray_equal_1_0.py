#!/usr/bin/python
# Given a boolean array with 1s and 0s, find the largest subarray with equal number
# of 1s and 0s.
import unittest

def replace(x):
    if x == 0: return -1
    return x

# Simple O(n^2) solution
def largestSubarrayNaive(arr):
    arr = map(replace, arr)
    best = 0
    for i in range(len(arr)):
        cur = arr[i]
        size = 1
        for j in range(i+1, len(arr)):
            size += 1
            cur += arr[j]
            if cur == 0:
                best = max(best, size)
    return best

def largestSubarray(arr):
    arr = map(replace, arr)
    sumLeft = []
    cur = 0
    for i in arr:
        cur += i
        sumLeft.append(cur)

    best = 0
    # Largest subarray starting from 0th index
    for i in range(len(sumLeft) - 1, 0, -1):
        if sumLeft[i] == 0:
            best = i + 1
            break

    # Largest subarray somewhere in the middle
    sumToPosition = {}
    for i in range(len(sumLeft)):
        if sumLeft[i] in sumToPosition:
            prevIdx = sumToPosition[sumLeft[i]]
            best = max(best, i - prevIdx)
        else:
            sumToPosition[sumLeft[i]] = i
    return best


class TestClass(unittest.TestCase):
    def test_0(self):
        arr = [0, 0]
        self.assertEqual(0, largestSubarrayNaive(arr))
        self.assertEqual(0, largestSubarray(arr))

    def test_1(self):
        arr = [0, 1]
        self.assertEqual(2, largestSubarrayNaive(arr))
        self.assertEqual(2, largestSubarray(arr))

    def test_2(self):
        arr = [0, 1, 1, 0, 0, 0]
        self.assertEqual(4, largestSubarrayNaive(arr))
        self.assertEqual(4, largestSubarray(arr))

    def test_3(self):
        arr = [0, 1, 1, 0, 0, 1, 1, 1]
        self.assertEqual(6, largestSubarrayNaive(arr))
        self.assertEqual(6, largestSubarray(arr))

    def test_4(self):
        arr = [0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
        self.assertEqual(8, largestSubarrayNaive(arr))
        self.assertEqual(8, largestSubarray(arr))

unittest.main()
