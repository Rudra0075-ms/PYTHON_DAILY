import csv
with open("csv_1/students.csv","r") as file:
    reader = csv.DictReader(file)
    

    for row in reader:
        if row["Branch"] == "CSE" or row["Branch"] == "AIML":
            print(row["Name"])
 

