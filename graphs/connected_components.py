#!/usr/bin/python
# Given a two-dimensional array representing a graph, with each
# item being either 'X' or '-', find the size of the largest connected
# component of 'X' characters.  Connections span up/down/left/right (not diagonal)
#
# e.g.,
#    X - - X
#    X X - -
#    - - - X
#
# Answer above is 3
import unittest

def dfs(G, vis, i, j):
    if i < 0 or j < 0 or i >= len(G) or j >= len(G[0]) or vis[i][j] or G[i][j] == '-':
        return 0
    vis[i][j] = True
    return 1 + dfs(G, vis, i-1, j) + dfs(G, vis, i+1, j) + dfs(G, vis, i, j-1) + dfs(G, vis, i, j+1)

def solution(G):
    N = len(G)
    M = len(G[0])
    vis = []
    for i in range(N):
        vis.append([False]*M)

    best = 0
    for i in range(N):
        for j in range(M):
            best = max(best, dfs(G, vis, i, j))

    return best

class TestClass(unittest.TestCase):
    def test_ex(self):
        G = ["X--X",
             "XX--",
             "---X"]
        self.assertEqual(3, solution(G))

    def test_diag(self):
        G = ["X-X-",
             "-X-X",
             "X-X-"]
        self.assertEqual(1, solution(G))

    def test_full(self):
        G = ["XXXX",
             "XXXX",
             "XXXX"]
        self.assertEqual(12, solution(G))

    def test_empty(self):
        G = ["----",
             "----",
             "----"]
        self.assertEqual(0, solution(G))
unittest.main()
