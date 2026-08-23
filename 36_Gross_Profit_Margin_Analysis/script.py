import pandas as pd

# 1. Load margin data
df = xl("Margin_Table[#All]", headers=True)

# 2. Calculate Gross Profit Margin Percentage
# Formula: (Gross Profit / Revenue) * 100
df['Margin_Pct'] = (df['Gross_Profit'] / df['Revenue']) * 100

# Display results
df