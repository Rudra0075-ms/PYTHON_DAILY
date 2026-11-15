days = int(input("Enter overdue days: "))

if days <= 5:
    fine = days * 2
elif days <= 10:
    fine = 10 + (days - 5) * 5
else:
    fine = 35 + (days - 10) * 10

if fine > 500:
    fine = fine + 100

print("Fine =", fine)

if fine <= 1000:
    print("Eligible to borrow books again")
else:
    print("Not eligible to borrow books again")

    
