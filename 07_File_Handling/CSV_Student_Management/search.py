import csv

search=input("Student Name= ")

with open("csv_1/students.csv","r",) as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].lower() == search.lower():
            print(row)
            break
    else:
        print("Not found!")

