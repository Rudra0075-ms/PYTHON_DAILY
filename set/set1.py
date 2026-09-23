def userset(set_name):
    elements = input(f"Enter elements for {set_name}: ").split()
    return set(elements)

def union(a, b):
    return a|b

def intersection(a, b):
    return a & b

def difference(a, b):
    return a-b

def symmetric_difference(a, b):
    return a ^ b

def display_results(a, b):
    print(f"Set A               : {a}")
    print(f"Set B               : {b}")
    print(f"Union (A | B)       : {union(a, b)}")
    print(f"Intersection (A & B): {intersection(a, b)}")
    print(f"Difference (A - B)  : {difference(a, b)}")
    print(f"Difference (B - A)  : {difference(b, a)}")
    print(f"Symmetric Diff(A^B) : {symmetric_difference(a, b)}")

a = userset("a")
b = userset("b")
display_results(a, b)
