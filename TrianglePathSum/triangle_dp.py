#!/usr/bin/python

def printTriangle(rows):
    for i in range(len(rows)):
        thisRow = ""
        for j in range(len(rows[i])):
            thisRow += " " + str(rows[i][j])
        print thisRow

# O(row count) runtime
def dp(rows):
    costs = [0] * len(rows)
    for i in range(len(rows)):
        costs[i] = [0] * len(rows[i])

    for j in range(len(rows[len(rows)-1])):
        costs[i][j] = int(rows[i][j])

    for i in range(len(rows) - 2, -1, -1):
        for j in range(len(rows[i])):
            costs[i][j] = int(rows[i][j]) + max(costs[i+1][j], costs[i+1][j+1])

    return costs[0][0]

# Test
rows = [[5], [9, 6], [4, 6, 8], [0, 7, 1, 5]]
print str(dp(rows))

rows = []
fh = open('triangle.txt')
for row in fh:
    rows.append(row.split())
printTriangle(rows)

print str(dp(rows))
