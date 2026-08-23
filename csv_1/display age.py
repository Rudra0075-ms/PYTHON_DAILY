import csv

with open("csv_1/students.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if int(row["Age"]) > 19:
            print(row)

