sentence = input("Enter a sentence: ")
words = sentence.split()
rev_w = [word[::-1] for word in words]
search = input("Enter word to search: ")
count = words.count(search)
for i in range(len(rev_w)):
    if i % 2 == 0:
        rev_w[i] = rev_w[i].upper()
print("Reversed words:", " ".join(rev_w))
print("Occurrences of", search, ":", count)
print("Final modified sentence:", " ".join(rev_w))
