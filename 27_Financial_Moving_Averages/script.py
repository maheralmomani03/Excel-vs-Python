import pandas as pd
df = xl("Trends_Table[#All]", headers=True)

# Calculating 7-Day Moving Average to smooth sales data
df['7_Day_MA'] = df['Sales'].rolling(window=7).mean()
df