import pandas as pd

df = pd.read_excel(r"/Users/ialinaok/Documents/python/ibm-data-analysis/pandas/Customer Call List.xlsx")
df = df.drop_duplicates()
df = df.drop(columns="Not_Useful_Column")
df["Last_Name"] = df["Last_Name"].str.strip("123/_.")
df["Phone_Number"] = df["Phone_Number"].str.replace("[^a-zA-Z0-9]","", regex=True)
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: str(x))
df["Phone_Number"] = df["Phone_Number"].apply(lambda x: x[0:3] + '-' + x[3:6] + '-' + x[6:10])
df["Phone_Number"] = df["Phone_Number"].str.replace("Na--", "N")
df["Phone_Number"] = df["Phone_Number"].str.replace("nan--", "N")
df[["Street_Address", "State", "Zip_Code"]] = df["Address"].str.split(",", n=2, expand=True)
df["Paying Customer"] = df["Paying Customer"].str.replace("Yes", "Y")
df["Paying Customer"] = df["Paying Customer"].str.replace("No", "N")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("Yes", "Y")
df["Do_Not_Contact"] = df["Do_Not_Contact"].str.replace("No", "N")
df = df.fillna('N')
for x in df.index:
    if df.loc[x, "Do_Not_Contact"] == 'Y':
        df.drop(x, inplace=True)
for y in df.index:
    if df.loc[y, "Phone_Number"] == 'N':
        df.drop(y, inplace=True)
df = df.reset_index(drop=True)

print(df)