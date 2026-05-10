import pandas as pd
df = xl("Stock_Table[#All]", headers=True)
df['Daily_Return'] = df['Close'].pct_change().fillna(0) * 100
df