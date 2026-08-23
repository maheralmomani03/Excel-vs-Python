import pandas as pd
df = xl("Income_Statement[#All]", headers=True)

# Vertical Analysis: All items as a percentage of Total Revenue
total_sales = df.iloc[0]['Amount']
df['Pct_of_Sales'] = (df['Amount'] / total_sales) * 100
df