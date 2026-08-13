email = input("Enter email address: ")
uname, domain = email.split("@")
ext = "." + domain.split(".")[-1]
print("Username:", uname)
print("Domain:", domain)
print("Domain Extension:", ext)
new_domain = input("Enter new domain: ")
mod_email = uname + "@" + new_domain + ext
lttr = dig = spcl = 0
for ch in email:
    if ch.isalpha():
        lttr += 1
    elif ch.isdigit():
        dig += 1
    else:
        spcl += 1
print("Letters:", lttr)
print("Digits:", dig)
print("Special Symbols:", spcl)
print("Modified Email:", mod_email)
