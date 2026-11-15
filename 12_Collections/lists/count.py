n=[12,45,3,67,8,9]
e,o=0,0

for i in n:
    if i%2==0:
        e+=1
    else:
        o+=1
print(f"even count = {e} and odd count = {o}")            

