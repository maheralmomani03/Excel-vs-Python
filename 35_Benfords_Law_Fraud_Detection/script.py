import pandas as pd

# 1. Load transaction data
df = xl("Fraud_Table[#All]", headers=True)

# 2. Extract the first digit of the transaction amount
df['First_Digit'] = df['Amount'].astype(str).str[0]

# 3. Count frequency of each first digit (Forensic Audit)
df.groupby('First_Digit').size()