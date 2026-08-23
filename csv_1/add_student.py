import csv

name= input("Name= ")
age= input("Age= ")
branch = input("Branch= ")

with open("csv_1/students.csv", "a", newline="\n") as file:
    writer = csv.writer(file)
    writer.writerow([name,age,branch])
    
print("Student added!!!")


