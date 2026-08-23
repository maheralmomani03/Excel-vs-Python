import pandas as pd

# 1. Load inventory and purchase data
df = xl("COGS_Table[#All]", headers=True)

# 2. Calculate Cost of Goods Sold (COGS)
# Formula: Opening Inv + Purchases - Closing Inv
df['COGS'] = df['Beg_Inv'] + df['Purchases'] - df['End_Inv']

# Display inventory report
df[['Item', 'COGS']]