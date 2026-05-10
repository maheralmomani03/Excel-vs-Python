import pandas as pd
df = xl("Date_Table[#All]", headers=True)
df.columns = df.columns.str.strip()

# Standardizing messy dates into one unified format
df['Clean_Date'] = pd.to_datetime(df['Raw_Date'], errors='coerce', dayfirst=True)
df