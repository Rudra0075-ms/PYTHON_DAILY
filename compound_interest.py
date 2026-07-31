p = int(input("principal amount:"))
r = float(input("rate of interest:"))
t = int(input("time period:"))
a = p*(1+r/100)**t
print("compound interest (ci) = ", a - p)
