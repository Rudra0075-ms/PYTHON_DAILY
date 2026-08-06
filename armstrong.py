n = int(input("Enter the limit: "))

count = 0

print("Armstrong numbers are:")

for i in range(10, n + 1):
    temp = i
    digits = len(str(i))
    s = 0

    while temp > 0:
        rem = temp % 10
        s = s + rem ** digits
        temp //= 10

    if s == i:
        print(i, end=" ")
        count += 1

print("\nTotal Armstrong numbers =", count)

