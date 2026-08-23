import pandas as pd

# 1. Load fixed costs and weighted margin data
df = xl("BEP_Multi_Table[#All]", headers=True)

# 2. Calculate Weighted Average Break-Even Units
# Formula: Fixed Costs / Weighted Average Contribution Margin
df['BE_Units'] = df['Fixed_Costs'] / df['WA_Margin']

# Display break-even results
df