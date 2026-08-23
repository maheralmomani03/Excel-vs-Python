import pandas as pd

# 1. Load historical revenue data
df = xl("Revenue_Table[#All]", headers=True)

# 2. Calculate Quarter-over-Quarter Growth Percentage
df['Growth_Pct'] = df['Revenue'].pct_change() * 100

# Display performance analysis
df