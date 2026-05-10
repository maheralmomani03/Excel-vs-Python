import pandas as pd
df = xl("Profit_Table[#All]", headers=True)
df['CM_Unit'] = df['Price'] - df['Variable_Cost']
df[['Product', 'CM_Unit']]