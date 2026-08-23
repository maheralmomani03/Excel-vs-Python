import pandas as pd

# 1. Load asset cost data
df = xl("Salvage_Table[#All]", headers=True)

# 2. Estimate Salvage Value (10% of Cost)
df['salvage_estimate'] = df['Cost'] * 0.10

# Display updated asset valuation
df