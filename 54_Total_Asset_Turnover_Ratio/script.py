import pandas as pd

# 1. Load financial position and sales data
df = xl("Asset_Turnover_Table[#All]", headers=True)

# 2. Calculate Asset Turnover Ratio
# Formula: Net Sales / Total Assets
df['turnover'] = df['Sales'] / df['Total_Assets']

# Display efficiency report
df