emp = float(input("Enter Monthly/Basic Salary (Rs): "))

print("\n----------- Salary Details -----------")
print("Basic Salary =", emp)

hra = emp * 20 / 100
da = emp * 15 / 100
pf = emp * 12 / 100

print("HRA (20%) =", hra)
print("DA (15%) =", da)
print("PF (12%) =", pf)

gross_salary = emp + hra + da
print("Gross Salary =", gross_salary)

net_salary = gross_salary - pf
print("Net Salary =", net_salary)

print("\nComparison (Net Salary > Rs.50000):", net_salary > 50000)

if net_salary > 50000:
    print("Employee earns more than Rs.50000.")
else:
    print("Employee does not earn more than Rs.50000.")
