punc = '''!(){}[]-=+*/.<>?|\@#$%^&~`:;'''
txt = input("string=")
res=""
for ch in txt:
    if ch not in punc:
        res+=ch
print(res)        
