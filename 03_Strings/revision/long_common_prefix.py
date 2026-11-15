words= ["flower", "flow", "flight"]
prefix= words[0]
for word in words[1:]:
    while not word.startswith(prefix):
        prefix= prefix[:-1]
print(prefix)    

#Keep removing the last character until every string starts with the same prefix.

