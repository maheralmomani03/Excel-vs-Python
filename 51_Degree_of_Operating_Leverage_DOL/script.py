import pandas as pd

# 1. Load operating data
df = xl("DOL_Analysis[#All]", headers=True)

# 2. Calculate Degree of Operating Leverage (DOL)
# Formula: Contribution Margin / Operating Income
df['DOL'] = df['Contribution_Margin'] / df['Operating_Income']

# Display risk analysis report
df