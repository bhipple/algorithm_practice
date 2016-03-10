#!/usr/bin/python

class Person():
    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __repr__(self):
        return "Person: %s, %s" % (self.age, self.name)

def compare(a, b):
    if a.age < b.age:
        return -1
    if a.age > b.age:
        return 1
    if a.name < b.name:
        return -1
    if a.name > b.name:
        return 1
    return 0


a = Person(20, "Ben")
b = Person(20, "Adam")
c = Person(15, "Dave")
d = Person(27, "Cynthia")

print sorted([a,b,c,d], cmp=compare)
