#!/usr/bin/python
# Given a string, reverse the word order
import unittest


# Reverse everything in [i, j)
def reverse(s, i, j):
    j -= 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

# Strings aren't mutable in Python, so we'll convert it to a list and pretend
# we're coding in C with a char*
def solution(s):
    s = list(s)

    # Reverse the whole list
    reverse(s, 0, len(s))

    # Reverse each word
    thisWordStart = 0
    for k in range(len(s)+1):
        if k == len(s) or s[k] == ' ':
            reverse(s, thisWordStart, k)
            thisWordStart = k+1

    return "".join(s)


class TestClass(unittest.TestCase):
    def test_a(self):
        a = "My name is Ben."
        self.assertEqual("Ben. is name My", solution(a))

    def test_b(self):
        b = "Hello this is a sentence"
        self.assertEqual("sentence a is this Hello", solution(b))

    def test_c(self):
        c = "Not  bothering      to  handle   whitespace   efficiently"
        self.assertEqual("efficiently   whitespace   handle  to      bothering  Not", solution(c))

unittest.main()
