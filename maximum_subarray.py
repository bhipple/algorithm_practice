#!/usr/bin/python
# https://en.wikipedia.org/wiki/Maximum_subarray_problem
# Given a list, find the largest sum of a contiguous subarray.

# Kadane's algorithm
def maxSubarray(arr):
    best = 0
    current = 0
    for i in range(len(arr)):
        current = max(current + arr[i], 0)
        best = max(best, current)
    return best

print maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
