#!/usr/bin/python
# Given two rectangles, determine if they overlap
import unittest

class Rectangle(object):
    def __init__(self, blX, blY, trX, trY):
        self.blX = blX
        self.blY = blY
        self.trX = trX
        self.trY = trY

def overlaps(r1, r2):
    if r1.blX >= r2.trX or \
       r1.trX <= r2.blX or \
       r1.blY >= r2.trY or \
       r1.trY <= r2.blY:
       return False
    return True

class TestClass(unittest.TestCase):
    def test_1(self):
        r1 = Rectangle(0, 0, 5, 5)
        r2 = Rectangle(-1, -1, 2, 2)
        self.assertTrue(overlaps(r1, r2))

    def test_2(self):
        r1 = Rectangle(0, 0, 5, 5)
        r2 = Rectangle(-2, -2, -1, -1)
        self.assertFalse(overlaps(r1, r2))

    def test_adjacent(self):
        r1 = Rectangle(0, 0, 1, 1)
        r2 = Rectangle(1, 1, 2, 2)
        self.assertFalse(overlaps(r1, r2))

unittest.main()
