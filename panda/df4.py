import pandas as pd

data = {"Name": ["tom", "jerry", "spike"],"Age":[7,6,9]}

df = pd.DataFrame(data, index = ["a","b","c"])

df["Job"] = ["cat", "mouse", "dog"]

new_rows = pd.DataFrame([{"Name": "Billie", "Age": 28, "Job": "Engineer"},{"Name": "Hero", "Age": 18, "Job": "Chef"}], index=["d",""])

df = pd.concat([df, new_rows])

print(df)

print(df.iloc[0])


