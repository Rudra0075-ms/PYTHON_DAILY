import pandas as pd

data = pd.read_csv("csv_1/students.csv")

data = data.sort_values("Age")

data.to_csv("csv_1/sorted_students.csv", index=False)

print("Students Arranged!!!")
