n= [10,20,10,30,90,60,40,20,50,10]

n1= []

for i in n:
    if n.count(i) > 1 and i not in n1:
        n1.append(i)

print("duplicate elements= ", n1)

