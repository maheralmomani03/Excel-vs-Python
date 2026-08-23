import pandas as pd

# 1. Load branch sales data
df = xl("Rank_Table[#All]", headers=True)

# 2. Sort branches by sales in descending order
df_sorted = df.sort_values(by='Total_Sales', ascending=False)

# Display sorted performance ranking
df_sorted