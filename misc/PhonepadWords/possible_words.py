#!/usr/bin/python
import enchant

d = enchant.Dict("en_US")

keyToLetters = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i'],
    ['j', 'k', 'l'],
    ['m', 'n', 'o'],
    ['p', 'q', 'r', 's'],
    ['t', 'u', 'v'],
    ['w', 'x', 'y', 'z']
]

class Node:
    def __init__(self, let):
        self.letter = let
        self.children = []

def intToListOfNodes(x):
    res = []

    for letter in keyToLetters[x - 2]:
        res.append(Node(letter))

    return res

def phoneWords(head, x):
    if not len(x) > 0:
        return None

    head.children = intToListOfNodes(int(x[0]))

    if not head.children == None:
        for child in head.children:
            phoneWords(child, x[1:])


# Testing
def printPath(head, sofar):
    if head == None:
        return
    if head.children == None or not len(head.children):
        if d.check(sofar + head.letter):
            print sofar + head.letter
        return

    for child in head.children:
        printPath(child, sofar + head.letter)



x = input("Enter a phonepad sequence: ")

head = Node(' ')
phoneWords(head, str(x))
printPath(head, "")
