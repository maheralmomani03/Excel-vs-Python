import pandas as pd

# 1. Load profit sensitivity data
df = xl("Sensitivity_Table[#All]", headers=True)

# 2. Calculate New Profit after cost increase
# Formula: Base Profit * (1 - Cost Increase %)
df['new_profit'] = df['Base_Profit'] * (1 - df['Cost_Increase'])

# Display impact analysis
df