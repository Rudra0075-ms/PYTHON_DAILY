import pandas as pd

data = pd.read_csv("csv_1/students.csv")

data.to_excel("csv_1/students.xlsx", index=False)

print("Excel file created!!!")

