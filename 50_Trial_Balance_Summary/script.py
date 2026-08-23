import pandas as pd

# 1. Load raw Trial Balance data
df = xl("Trial_Balance[#All]", headers=True)

# 2. Summarize balances by Account Type (Pivot logic)
summary = df.groupby('Account_Type')['Balance'].sum()

# Display summarized view for Financial Statements
summary