import pandas as pd

# 1. Load Sales and Prices data from Excel Tables
sales = xl("Sales_Table[#All]", headers=True)
prices = xl("Prices_Table[#All]", headers=True)

# 2. Merge dataframes on 'SKU_ID' (The professional alternative to VLOOKUP/XLOOKUP)
df = pd.merge(sales, prices, on="SKU_ID")

# 3. Calculate Total Sales Amount
df['Total'] = df['Qty'] * df['Price']

# Display merged result with totals
df