#Clean Data Code
df = xl("Table1[#All]", headers=True)
df['Customer_Name'] = df['Customer_Name'].str.strip().str.title()
df