num = (45, 12, 89, 23, 7, 65, 89, 12)
print("Tuple= ", num)

def sort_tuple(t, descending=False):
    return tuple(sorted(t, reverse=descending))

def search_element(t, key):
    if key in t:
        return f"{key} found at index {t.index(key)}"
    return f"{key} not found"

def second_large_small(t):
    unique = sorted(set(t))
    if len(unique) >= 2:
        return unique[-2], unique[1]
    return None, None

print("Sorted = ", sort_tuple(num))
print("Reversed = ", sort_tuple(num, descending=True))

target = 23
print("Search = ", search_element(num, target))

second_large, second_small = second_large_small(num)
print("2nd Largest Element = ", second_large)
print("2nd Smallest Element = ", second_small)

