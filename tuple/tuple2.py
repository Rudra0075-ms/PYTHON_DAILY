def find_union(t1, t2):
    return tuple(set(t1) | set(t2))

def find_common(t1, t2):
    return tuple(set(t1) & set(t2))

def find_only_first(t1, t2):
    return tuple(set(t1) - set(t2))

def find_max(t):
    return max(t)

def find_min(t):
    return min(t)

t1 = (1, 2, 3, 4, 5)
t2 = (4, 5, 6, 7, 8)

print("Tuple 1:", t1)
print("Tuple 2:", t2)

print("Union:", find_union(t1, t2))
print("Common elements:", find_common(t1, t2))
print("Only in Tuple 1:", find_only_first(t1, t2))
print("Tuple 1 Max:", find_max(t1),"Min:", find_min(t1))
print("Tuple 2 Max:", find_max(t2),"Min:", find_min(t2))
