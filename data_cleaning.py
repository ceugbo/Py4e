import pandas as pd

df = pd.read_csv("data.csv")

#Drop irrelevant columns
# df = df.drop(columns=["Legendary", "No"])
# print(df)


#Replacing null values
# df = df.dropna(subset=["Type2"])
# print(df)

df = df.fillna({"Type2": "None"})
# print(df.to_string())

#Fixing Inconsistent Values
# df["Type1"] = df["Type1"].replace({"Grass": "GRASS"})
# print(df.to_string())

#Standardize Text
# df["Name"] = df["Name"].str.lower()
# print(df.to_string())

#Change Data type
# df["Legendary"] = df["Legendary"].astype(bool)
# print(df.to_string())

#Remove redundant data
df = df.drop_duplicates()
print(df.to_string())