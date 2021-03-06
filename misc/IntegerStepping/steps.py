#!/usr/bin/python
# Naive solution that works with suboptimal results
MAX_INT = 2000000000

def steps(X):
    n = 1
    while n*(n+1)/2 <= X:
        n += 1
    n -= 1
    rem = X - n*(n+1)/2
    return n + 2*rem

# Recursive solution that gives optimal results but needs a base case,
# provided by the naive solution
def maze(source, step, destination, upperLim):
    if source == destination:
        return step
    if step > upperLim:
        return -1
    step += 1
    plus = maze(source+step, step, destination, upperLim)
    minus = maze(source-step, step, destination, upperLim)

    if plus > 0:
        if minus > 0:
            return min(plus, minus)
        return plus
    if minus > 0:
        return minus
    return -1

def combined(destination):
    upperLim = steps(destination)
    return maze(0, 0, destination, upperLim)

# This uses the intution that it should not be necessary to
# go past the destination and backtrack, and that provides
# the recursive base case.
def good(source, step, destination):
    if source == destination:
        return step
    if abs(source) > destination:
        return MAX_INT
    step += 1
    plus = good(source+step, step, destination)
    minus = good(source-step, step, destination)
    return min(plus, minus)

for i in range(22):
    print "It takes %s steps to get to %s" % (combined(i), i)
