import pandas as pd

data = {
    "Name": ["Spongebob", "Patrick", "Squidward"],
    "Age": [30, 35, 50]
    }
df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

#Add a new col
df["Job"] = ["Cook", "N/A", "Cashier"]
df["Salary"] =  [110000, 90000, 120000]

#Add a new rows
new_rows = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer", "Salary": 150000}, {"Name": "Eugene", "Age": 60, "Job": "Manager", "Salary": 200000}], index=["Employee 4", "Employee 5"])
df = pd.concat([df, new_rows])

print(df)