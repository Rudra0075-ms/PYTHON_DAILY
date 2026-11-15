#Count consecutive repeated characters and store the character with its count.

s= input("string= ")
result= ""
c=1
for i in range(len(s)):
    if i +1 < len(s) and s[i] == s[i+1]:
        c+=1
    else:
        result+=s[i]+str(c)
        c=1
print("result= ",result)


#Input: aaabbc

#Output: a3b2c1


