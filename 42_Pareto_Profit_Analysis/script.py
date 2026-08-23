import pandas as pd

# 1. Load and Sort customer profit data
df = xl("Pareto_Table[#All]", headers=True).sort_values(by='Profit', ascending=False)

# 2. Calculate Cumulative Profit Percentage
df['Cum_Pct'] = (df['Profit'].cumsum() / df['Profit'].sum()) * 100

# 3. Identify the "Top 80%" customers (Pareto Rule)
top_customers = df[df['Cum_Pct'] <= 80]
top_customers