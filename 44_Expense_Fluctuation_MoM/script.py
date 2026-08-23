import pandas as pd

# 1. Load monthly expense data
df = xl("MoM_Table[#All]", headers=True)

# 2. Calculate Month-over-Month (MoM) Percentage Change
df['MoM_Change_Pct'] = df['Amount'].pct_change() * 100

# Display fluctuation analysis
df