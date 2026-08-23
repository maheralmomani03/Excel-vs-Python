import pandas as pd

# 1. Load transaction data
df = xl("VAT_Table[#All]", headers=True)

# 2. Calculate VAT (5%)
df['VAT_5%'] = df['Net_Amount'] * 0.05

# Display final amounts for tax reporting
df