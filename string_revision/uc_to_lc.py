s= input("enter string= ")
s1= ""
for ch in s:
    if 'A' <= ch <= 'Z':
        s1+=chr(ord(ch)+32)
    else:
        s1+=ch 
print(s1)
           