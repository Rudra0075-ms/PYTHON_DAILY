import pandas as pd

calories = {"1":1750, "2":2100, "3":1500}

series = pd.Series(calories)

print(series)

series.loc["3"] += 50

print(series.loc["3"])

print(series[series<2000])
