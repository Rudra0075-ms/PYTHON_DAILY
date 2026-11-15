a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]

c= []

for i in a:
    if i in b:
        c.append(i)

print("Common elemnts= ", c)        
