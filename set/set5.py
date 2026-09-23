n = int(input("no. of elements = "))
numbers = set()

for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.add(num)

print("\nYour Set:", numbers)

large = max(numbers)
print("\nLargest element:", large)

small = min(numbers)
print("Smallest element:", small)

total = sum(numbers)
print("Sum of elements:", total)

avg = total / len(numbers)
print("Average of elements:", avg)

even = sum(1 for x in numbers if x % 2 == 0)
odd = sum(1 for x in numbers if x % 2 != 0)
print("Count of Even numbers:", even)
print("Count of Odd numbers:", odd)

search = int(input("\nEnter a number to search in the set: "))
if search in numbers:
    print(f"{search} EXISTS in the set.")
else:
    print(f"{search} does NOT exist in the set.")

print("\nSet in Sorted Order:", sorted(numbers))
