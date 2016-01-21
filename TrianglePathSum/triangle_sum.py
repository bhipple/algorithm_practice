#!/usr/bin/python

with open('triangle.txt', 'r') as f:
    triangle = map(lambda x: map(int, x.split()), f.readlines())

test = [ [1],
             [2,3],
             [4,5,6],
             [10,9,8,7]]

def heaviestPath(tri, row, col):
    if row >= len(tri) or col >= len(tri[row]):
        return 0
    return tri[row][col] + max(heaviestPath(tri, row+1, col), heaviestPath(tri, row+1, col+1))

print heaviestPath(test, 0, 0)

print heaviestPath(triangle, 0, 0)
