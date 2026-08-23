import pandas as pd

data = pd.read_csv("csv_1/students.csv")

data.to_json("csv_1/students.json", orient="records", indent=4)

print("JSON created!!!")

