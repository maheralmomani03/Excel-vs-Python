import pandas as pd

# 1. Load investment and NOPAT data
df = xl("EVA_Table[#All]", headers=True)

# 2. Calculate Economic Value Added (EVA)
# Formula: NOPAT - (WACC * Capital)
df['eva'] = df['NOPAT'] - (df['WACC'] * df['Capital'])

# Display value creation report
df