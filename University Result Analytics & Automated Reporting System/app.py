import pandas as pd
# from openpyxl.styles import Font, Alignment

df = pd.read_excel("raw_results.xlsx")
df = df.dropna(subset="Name")
df = df.drop_duplicates()

#Resolving invalid scores
invalid_rows = df[
    (df["Score"]<0)|
    (df["Score"]>100)|
    (df["Score"].isna())
]

#Getting the weighted grade points
gp_list = []
remark_list = []
for score in df["Score"]:
    if score >= 70:
        gp = 5
        remark = "A"
    elif 59< score < 70:
        gp = 4
        remark = "B"
    elif 49< score <60:
        gp = 3
        remark = "C"
    elif 44< score <50:
        gp = 2
        remark = "D"
    elif 39< score <45:
        gp = 1
        remark = "E"
    else:
        gp = 0
        remark = "F"
    gp_list.append(gp)
    remark_list.append(remark)

#Adding Grade and Grade Point column
df["Grade"] = remark_list
df["GP"] = gp_list

# unit_list = df["Units"].tolist()
df["WGP"] = df["GP"] * df["Units"]

df["Name"] = df["Name"].str.strip()
df["Matric No"] = df["Matric No"].str.strip()
group = df.groupby("Matric No")

matric_block = "nil"
gpa_dict = {}

for matric in df["Matric No"]:
    if matric_block == matric:
        continue
    matric_block = matric
    student = group.get_group(matric)
    wgp_sum = student["WGP"].sum()
    unit_sum = student["Units"].sum()
    gpa = round(wgp_sum/unit_sum, 2)
    print(student)
    print(f"Cummulative Weighted Grade Point = {wgp_sum}")
    print(f"Total Units Taken = {unit_sum}")
    print(f"GPA = {gpa}")
    gpa_dict[matric] = float(gpa)

# with pd.ExcelWriter("transcripts.xlsx", engine="openpyxl") as writer:
#         for matric, group in df.groupby("Matric No"):
#             group.to_excel(writer, sheet_name=str(matric), index=False)
#             ws = writer.sheets[str(matric)]
#             last_row = ws.max_row + 2
#             ws.merge_cells(start_row=last_row, start_column=1, end_row=last_row, end_column=6)
#             cell = ws.cell(row=last_row, column=1)
#             cell.value = f"GPA = {gpa}"
#             cell.font = Font(bold=True)
#             cell.alignment = Alignment(horizontal="center")
        
