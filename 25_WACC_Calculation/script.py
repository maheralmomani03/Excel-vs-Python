import pandas as pd
df = xl("WACC_Table[#All]", headers=True)

# Calculate Weight and WACC components
total_v = df['Equity'] + df['Debt']
df['WACC'] = (df['Equity']/total_v * df['Cost_E']) + (df['Debt']/total_v * df['Cost_D'] * (1 - df['Tax_Rate']))
df[['WACC']]