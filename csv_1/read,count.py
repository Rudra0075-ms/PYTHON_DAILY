import csv

c = 0

with open("csv_1/students.csv", "r") as file:
    data = csv.reader(file)
    data = csv.DictReader(file)

    for row in data:
        print(row)
        print(row["Name"])
        c+=1
print(f"Total Students={c}")        

        