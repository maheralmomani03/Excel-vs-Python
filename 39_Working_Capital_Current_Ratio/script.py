import pandas as pd

# 1. Load liquidity data
df = xl("Liquidity_Table[#All]", headers=True)

# 2. Calculate Current Ratio
# Formula: Current Assets / Current Liabilities
df['Current_Ratio'] = df['Current_Assets'] / df['Current_Liabilities']

# Display liquidity report
df