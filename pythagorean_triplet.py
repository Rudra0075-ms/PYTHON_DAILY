def triplet(a,b,c):
    sorted_no=sorted([a,b,c])
    return sorted_no[0]**2 + sorted_no[1]**2==sorted_no[2]**2
print(triplet(3,4,5))
