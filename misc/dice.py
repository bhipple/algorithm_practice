#!/bin/python
import random
# You are playing a dice game.  You toss two dice, and:
# - If the result is 7, you gain 1 dollar
# - If the result is even, you lose a dollar
# - If the result is odd and not 7, you restart the game.
#
# What is the expected value of this game?

ev = 0.0
trials = 0.0

def play():
    a = random.randint(1,6)
    b = random.randint(1,6)
    if a + b == 7:
        return 1.0
    if (a + b) % 2 == 0:
        return -1.0
    return play()

for i in range(10000000):
    trials += 1.0
    res = play()
    ev += res

    print "Trials: %d, Val: %f, Avg: %f" % (trials, ev, ev / trials)
