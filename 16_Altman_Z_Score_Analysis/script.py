import pandas as pd
df = xl("Z_Table[#All]", headers=True)
df.columns = df.columns.str.strip()

# Z-Score Formula: 1.2A + 1.4B + 3.3C + 0.6D + 1.0E
df['Z_Score'] = (1.2 * df['X1']) + (1.4 * df['X2']) + (3.3 * df['X3']) + (0.6 * df['X4']) + (1.0 * df['X5'])

df[['Company', 'Z_Score']]