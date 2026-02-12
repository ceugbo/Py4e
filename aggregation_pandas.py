import pandas as pd

df = pd.read_csv("data.csv")
# print (df)
group = df.groupby("Type1")
print(group["Height"].count())

# print(df.mean(numeric_only=True))

# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.count())