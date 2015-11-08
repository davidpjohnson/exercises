
def booolean(x, y, operation):

    if operation == "conjunction": return x & y
    if operation == "disjunction": return x | y
    if operation == "implication": return (1 ^ x) | y
    if operation == "exclusive":   return x ^ y
    if operation == "equivalence": return x ^ y ^ 1
    return 0


