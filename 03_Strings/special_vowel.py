def vow_replace(string,vowel):
    vowels="aeiou"
    res= ""
    for ch in string:
        if ch in vowels:
            res+=vowel
        else:
            res+=ch
    return res
print(vow_replace("apple mango","o"))
