#!/usr/bin/python3

from ex8 import boolean
import random 

boolean(1, 0, u"conjunction")
boolean(1, 0, u"disjunction")
boolean(1, 1, u"implication")
boolean(0, 1, u"exclusive")
boolean(0, 1, u"equivalence")
boolean(random.randrange(0, 2), random.randrange(0, 2), u"conjunction")
