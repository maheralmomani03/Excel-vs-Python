import pandas as pd

# 1. Load CVP data from Excel Table
df = xl("CVP_Table[#All]", headers=True)

# 2. Calculate Break-even Units
# Formula: Fixed Costs / (Selling Price - Variable Cost)
df['Break_Even'] = df['Fixed_Costs'] / (df['Selling_Price'] - df['Variable_Cost'])

# 3. Display specific results
df[['Product', 'Break_Even']]