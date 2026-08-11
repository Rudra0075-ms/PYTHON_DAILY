def amplify(n):
    return [n*10 if n%4==0 else n for n in range(1, n+1)]
print(amplify(5))

#Create a function that takes an integer and returns a list from 1 to the given number, where:
#1. If the number can be divided evenly by 4, amplify it by 10 (i.e. return 10 times the number).
#2. If the number cannot be divided evenly by 4, simply return the number
