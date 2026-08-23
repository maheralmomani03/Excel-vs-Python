import pandas as pd

# 1. Load inventory and cost data
df = xl("Inventory_Table[#All]", headers=True)

# 2. Calculate Inventory Turnover in Days
# Formula: (Average Inventory / COGS) * 365
df['Inv_Days'] = (df['Avg_Inv'] / df['COGS']) * 365

# Display inventory efficiency report
df