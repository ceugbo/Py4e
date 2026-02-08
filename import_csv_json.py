import pandas as pd

df = pd.read_csv("data.csv", index_col=["Name"])

#print(df.to_string())

# print(df.loc["Blastoise":"Pikachu", ["Height", "Weight"]])

# print(df.iloc[0:11:2, 0:3])
pokemon = input("Enter a pokemon name: ")
try:
    print(df.loc[pokemon])
except KeyError:
    print(pokemon + " not found")