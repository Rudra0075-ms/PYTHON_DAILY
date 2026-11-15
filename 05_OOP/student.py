name = input("Enter Full Name: ")
reg = input("Enter Registration Number: ")
dept = input("Enter Department: ")
email = input("Enter College Email ID: ")
s = name.replace(" ", "")
v = 0
cons = 0
for ch in s.lower():
    if ch in "aeiou":
        v += 1
    elif ch.isalpha():
        cons += 1
rev = name[::-1]
if s.lower() == s.lower()[::-1]:
    pali = "Yes"
else:
    pali = "No"
print("Name:", name)
print("Registration Number:", reg)
print("Department:", dept)
print("Email:", email)
print("Total characters:", len(s))
print("Vowels:", v)
print("Consonants:", cons)
print("Reversed Name:", rev)
print("Palindrome:", pali)
