#its like using pokedex
import pandas as pd

df = pd.read_csv("pokemon.csv")

print(df.to_string())

#selection by columns

print(df["Name"].to_string())

print(df["Height"].to_string())

print(df[["Name", "Height"]].to_string())

#selction by rows

print(df.loc[1:6:2])

df = df.set_index("Name")

print(df.loc["Charizard", ["Height","Weight"]])

pokemon = input("Pokemon Name = ")

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} ... not found")

