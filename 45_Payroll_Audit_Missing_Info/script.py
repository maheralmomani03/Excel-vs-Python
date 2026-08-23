import pandas as pd

# 1. Load payroll database
df = xl("Payroll_Table[#All]", headers=True)

# 2. Identify employees with missing critical info (Bank or Tax ID)
missing_info = df[df.isnull().any(axis=1)]

# Display employees needing data updates
missing_info