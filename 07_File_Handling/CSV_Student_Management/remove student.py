import csv

rem = input("Name = ").strip()

rows = []
found = False

with open("csv_1/students.csv", "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].strip().lower() == rem.lower():
            found = True
        else:
            rows.append(row)

if found:
    with open("csv_1/students.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Name", "Age", "Branch"]
        )

        writer.writeheader()
        writer.writerows(rows)

    print("Student removed!")
else:
    print("Student not found!")

    