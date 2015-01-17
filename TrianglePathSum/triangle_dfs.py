# O(2^(L-1)) runtime, where L is the depth of the DAG
def dfs(i, rowNum):
    if rowNum >= len(rows):
        return 0
    return rows[rowNum][i] + max(dfs(i, rowNum + 1), dfs(i + 1, rowNum + 1))


# Test
rows = [[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]]
print str(dfs(0, 0))
