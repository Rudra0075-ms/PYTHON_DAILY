import csv
students = []
with open("students.csv", "r") as file:
    data = csv.DictReader(file)
    for row in data:
        math = int(row["Math"])
        python = int(row["Python"])
        java = int(row["Java"])
        attendance = int(row["Attendance"])
        total = math + python + java
        percentage = total / 3
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"
        if math >= 40 and python >= 40 and java >= 40:
            status = "Pass"
        else:
            status = "Fail"
        if attendance >= 75:
            attendance_status = "Good"
        else:
            attendance_status = "Low"
        row["Total"] = total
        row["Percentage"] = round(percentage, 2)
        row["Grade"] = grade
        row["Status"] = status
        row["Attendance Status"] = attendance_status
        students.append(row)

topper = max(students, key=lambda x: float(x["Percentage"]))
fields = [
    "Name",
    "Math",
    "Python",
    "Java",
    "Attendance",
    "Total",
    "Percentage",
    "Grade",
    "Status",
    "Attendance Status"
]
with open("result.csv", "w", newline="") as file:

    writer = csv.DictWriter(file, fieldnames=fields)

    writer.writeheader()
    writer.writerows(students)
print("\n========== STUDENT REPORT ==========\n")

for student in students:

    print(
        student["Name"],
        "| Percentage:",
        student["Percentage"],
        "| Grade:",
        student["Grade"],
        "|",
        student["Status"],
        "| Attendance:",
        student["Attendance Status"]
    )

print("\n🏆 TOPPER")
print(
    topper["Name"],
    "-",
    topper["Percentage"],
    "%"
)

print("\n❌ FAILED STUDENTS")

for student in students:

    if student["Status"] == "Fail":
        print(student["Name"])

print("\n⚠️ LOW ATTENDANCE")

for student in students:

    if student["Attendance Status"] == "Low":
        print(student["Name"])


print("\n✅ Automation completed!")
print("📁 result.csv created successfully.")
