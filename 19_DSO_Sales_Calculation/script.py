import pandas as pd
df = xl("DSO_Table[#All]", headers=True)

# DSO Formula: (Receivables / Total Credit Sales) * 365
df['DSO'] = (df['Receivables'] / df['Annual_Sales']) * 365
df[['Customer', 'DSO']]