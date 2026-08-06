n = int(input("Enter the limit: "))

count = 0

print("Perfect numbers are:")

for i in range(1, n + 1):
    s = 0

    for j in range(1, i):
        if i % j == 0:
            s += j

    if s == i:
        print(i, end=" ")
        count += 1

print("\nTotal Perfect Numbers =", count)
