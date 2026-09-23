def calc_total(marks):
    return sum(marks)

def calc_percent(marks):
    total = sum(marks)
    return (total / (len(marks) * 100)) * 100

def calc_avg(marks):
    return sum(marks) / len(marks)

def calc_max(marks):
    return max(marks)

def calc_min(marks):
    return min(marks)

marks_list = []
print("Full marks = 100")
for i in range(1, 6):
    m = float(input(f"marks{i}= "))
    marks_list.append(m)

marks = tuple(marks_list)

total = calc_total(marks)
percentage = calc_percent(marks)
avg = calc_avg(marks)
highest = calc_max(marks)
lowest = calc_min(marks)

print(f"Marks (Tuple) : {marks}")
print(f"Total Marks   : {total} / 500")
print(f"Percentage    : {percentage:.2f}%")
print(f"Average Marks : {avg:.2f}")
print(f"Highest Marks : {highest}")
print(f"Lowest Marks  : {lowest}")

