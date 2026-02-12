import pandas as pd

df = pd.read_csv("data.csv", index_col=["Name"])

#print(df.to_string())

# print(df.loc["Blastoise":"Pikachu", ["Height", "Weight"]])

print(df.iloc[0:11:2, 0:3])
# pemon = input("Enter a pokemon name: ")
# ty:
    #  print(df.loc[pokemon])
# exct KeyError:
    # print(pokemon + " not found")