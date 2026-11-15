n = int(input("Number of integers =  "))

integers = set()
for i in range(n):
    num = int(input(f"Enter integer {i+1}: "))
    integers.add(num)

even_set = {x for x in integers if x % 2 == 0}
odd_set  = {x for x in integers if x % 2 != 0}

print("Original Set :", integers)
print("Even Numbers :", even_set)
print("Odd Numbers  :", odd_set)
