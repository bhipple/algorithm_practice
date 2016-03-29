#!/usr/bin/python
# Given an input string of numbers and an encoding such that
# '0' -> 'a', '1' -> 'b', ... '25' -> 'z'
# find how many possible decodings of the string exist.
import unittest

# Simple list eater implementation
# Can be made better with memoization
def eater(s):
    if not s or s == "" or len(s) == 1:
        return 1
    if int(s[0:2]) <= 25:
        return eater(s[1:]) + eater(s[2:])
    return eater(s[1:])

# Same as above, but it returns all results instead of merely counting them.
def eaterWithResults(s):
    if not s or s == "":
        return [""]
    if len(s) == 1:
        return [s]

    res = map(lambda x: s[0] + x, eaterWithResults(s[1:]))
    if int(s[0:2]) <= 25:
        return res + map(lambda x: "'" + s[0:2] + "'" + x, eaterWithResults(s[2:]))
    return res

## ============================================================================
## Tests
## ============================================================================
class Test(unittest.TestCase):
    def test_1(self):
        t = "1"
        self.assertEqual(1, eater(t))
        self.assertEqual(len(eaterWithResults(t)), eater(t))

    def test_2(self):
        t = "23"
        self.assertEqual(2, eater(t))
        self.assertEqual(len(eaterWithResults(t)), eater(t))

    def test_3(self):
        t = "123"
        self.assertEqual(3, eater(t))
        self.assertEqual(len(eaterWithResults(t)), eater(t))

    def test_4(self):
        t = "2123"
        self.assertEqual(5, eater(t))
        self.assertEqual(len(eaterWithResults(t)), eater(t))

    def test_5(self):
        t = "167"
        self.assertEqual(2, eater(t))
        self.assertEqual(len(eaterWithResults(t)), eater(t))

if __name__ == "__main__":
    unittest.main()
