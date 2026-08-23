import pandas as pd

# 1. Load marketing campaign data
df = xl("ROI_Table[#All]", headers=True)

# 2. Calculate ROI (Return on Investment)
# Formula: (Gain - Investment) / Investment
df['ROI'] = (df['Gain'] - df['Investment']) / df['Investment']

# Display results
df