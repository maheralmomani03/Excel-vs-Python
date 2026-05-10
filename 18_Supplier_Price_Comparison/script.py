import pandas as pd
df = xl("Price_Table[#All]", headers=True)
df.columns = df.columns.str.strip()

# Finding the row with the minimum price for each product
lowest_prices = df.loc[df.groupby('Product')['Price'].idxmin()]
lowest_prices[['Product', 'Supplier', 'Price']]