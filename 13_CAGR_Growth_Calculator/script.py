import pandas as pd
df = xl("Investment_Growth[#All]", headers=True)
start_val, end_val, periods = df['Investment_Value'].iloc[0], df['Investment_Value'].iloc[-1], 5
cagr = (end_val / start_val) ** (1 / periods) - 1
f"The CAGR is: {cagr:.2%}"