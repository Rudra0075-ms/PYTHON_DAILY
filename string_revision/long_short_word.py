s= input("sentence= ")
wrd= s.split()
print(max(wrd, key=len))
print(min(wrd, key=len))
