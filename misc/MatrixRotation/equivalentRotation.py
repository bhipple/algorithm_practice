#!/usr/bin/python

X1 = [[1,2,3], [4,5,6], [7,8,9]]
Y1 = [[1,2,3], [4,5,4], [3,2,1]]


def checkRotationEquality(X):
    n = len(X)
    for i in range(n):
        for j in range(n):
            if X[i][j] != X[n-i-1][n-j-1]:
                return False
    return True


def rotate180(X):
    n = len(X)
    Y = []
    for row in X:
        Y.append(list(row))

    for i in range(n):
        for j in range(n):
            Y[i][j] = X[n-i-1][n-j-1]

    return Y


def printMatrix(X):
    for row in X:
        print row
    print "\n"

print checkRotationEquality(X1)
print checkRotationEquality(Y1)

printMatrix(X1)
printMatrix(rotate180(X1))
