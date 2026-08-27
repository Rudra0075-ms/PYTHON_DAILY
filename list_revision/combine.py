a= [10,20,30,40]
b= [30,40,50,60]

c= a + b
d= []

for i in c:
    if i not in d:
        d.append(i)

print("Combined= ",c)
print("Without duplicates= ",d)

