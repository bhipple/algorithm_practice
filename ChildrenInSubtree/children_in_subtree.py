class Node:
    left = 0
    right = 0

def childCount(head):
    if not head:
        return 0
    return 1 + childCount(head.left) + childCount(head.right)

A = Node()
B = Node()
C = Node()
D = Node()
E = Node()
F = Node()
G = Node()

A.left = B
A.right = C
B.left = D
B.right = G
C.right = F
D.right = E

"""
          A
       B     C
     D   G     F
      E
"""

print "Child count of A is: " + str(childCount(A))
print "Child count of B is: " + str(childCount(B))
print "Child count of C is: " + str(childCount(C))
print "Child count of D is: " + str(childCount(D))
print "Child count of E is: " + str(childCount(E))
print "Child count of F is: " + str(childCount(F))
print "Child count of G is: " + str(childCount(G))
