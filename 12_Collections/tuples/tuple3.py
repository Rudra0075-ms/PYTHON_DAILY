t = tuple(map(int, input("Enter integers separated by space: ").split()))

def count_element(t, x):
    return t.count(x)

def frequency(t):
    for x in set(t):
        print(x, ":", t.count(x))

def most_frequent(t):
    return max(set(t), key=t.count)

def occur_once(t):
    print("Elements occurring only once:")
    for x in set(t):
        if t.count(x) == 1:
            print(x, end=" ")

x = int(input("Enter element to count: "))

print("Occurrence of", x, ":", count_element(t, x))

print("\nFrequency of every element:")
frequency(t)

print("\nMost frequently occurring element:", most_frequent(t))

occur_once(t)
