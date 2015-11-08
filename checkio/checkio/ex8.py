#!/usr/bin/python3
def boolean(x, y, operation):
    if operation == u"conjunction":
        if x == 1 and y == 1:
            print ("1")
        else:
            print ("0")
    if operation == u"disjunction":
        if x == 0 and y == 0:
            print ("0")
        else:
            print ("1")
    if operation == u"implication":
        if x == 1 and y == 0:
            print ("0")
        else:
            print ("1")

    if operation == u"exclusive":
        if x == y:
            print ("0")
        else:
            print ("1")
    if operation == u"equivalence":
        if x == y:
            print ("1")
        else:
            print("0")
