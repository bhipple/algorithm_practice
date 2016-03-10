#!/usr/bin/python
# Career Cup Bloomberg
# http://www.careercup.com/question?id=5687263784599552
# Given a sorted list containing duplicates, do an in-place
# conversion to a set (don't care about remaining elements
# in the list after the last unique element).

def compact(arr):
    lastIdx = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            lastIdx += 1
        arr[lastIdx] = arr[i]
    return arr

print compact([3, 3, 4, 5, 5, 6, 7, 7, 7])
