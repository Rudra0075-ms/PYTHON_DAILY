def ascii_EVEN(ip_str):
    res= ""
    for char in ip_str:
        if ord(char)%2==0:
            res+=char.upper()
        else:
            res+=char.lower()
    return res 
print(ascii_EVEN("do what floats you to do"))        
