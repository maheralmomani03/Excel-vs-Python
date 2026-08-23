import pandas as pd

# 1. Load the Executive KPI data
df = xl("KPI_Table[#All]", headers=True)

# 2. Calculate Current Ratio for ALL entities (Vectorized like Excel)
# Formula: Assets / Liabilities
df['Current_Ratio'] = df['Current_Assets'] / df['Current_Liabilities']

# 3. Executive summary print (Focus on Head Office)
ho_ratio = df.iloc[0]['Current_Ratio']
print(f"Executive Alert: Head Office Liquidity is {ho_ratio:.2f}")

# Display full dashboard table
df