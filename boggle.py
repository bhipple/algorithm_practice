#!/usr/bin/python
# Solve the game of Boggle: given a matrix of letters, find all dictionary words
# starting from a particular position.
import unittest
import enchant

def dfs(B, i, j, vis):
    if i < 0 or i >= len(B) or j < 0 or j >= len(B[0]) or vis[i][j]:
        return [""]

    vis[i][j] = True
    res = dfs(B, i-1, j, vis) \
          + dfs(B, i+1, j, vis) \
          + dfs(B, i, j-1, vis) \
          + dfs(B, i, j+1, vis)

    res = map(lambda x: B[i][j] + x, set(res))
    vis[i][j] = False
    return res

def solution(B, i, j):
    vis = []
    for k in range(len(B)):
        vis.append([False]*len(B[0]))
    res = dfs(B, i, j, vis)

    d = enchant.Dict('en_US')
    res = filter(d.check, res)
    return res

class TestClass(unittest.TestCase):
    def test_simple(self):
        B = [["a", "t", "a"],
             ["l", "e", "f"],
             ["d", "d", "i"]]

        res = solution(B, 1, 2)
        print res

unittest.main()
