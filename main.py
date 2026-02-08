import pandas as pd

data =[100, 102, 104, 200, 202]

series = pd.Series(data, index=["a", "b", "c", "d", "e"])

# series.loc["c"] = 200

print(series)