import pandas as pd

numbers = [10, 20, 30, 40, 50]

s = pd.Series(numbers, index=['a', 'b', 'c', 'd', 'e'])

s.loc["c"] = 25

print(s.loc["a"])
print(s.iloc[2])
print(s)


#df is data frame 
#DataFrame = A tabular data structure with rows AND columns. (2 Dimensional)
#Similar to an Excel spreadsheet
#loc[] is used to access the value by index
#iloc[] is used to access the value by position

