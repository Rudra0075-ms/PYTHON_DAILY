s= input("enter ur string= ")
uc=0
lc=0
dig=0
for ch in s:
    if ch.isupper():
        uc+=1
    elif ch.islower():
        lc+=1
    else:
        dig+=1        
print("upper count is ",uc)
print("lower count is ",lc)
print("digit count is ",dig)        
