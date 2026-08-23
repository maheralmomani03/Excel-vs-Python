import pandas as pd

# 1. Load multi-currency transaction data
df = xl("Transaction_Table[#All]", headers=True)

# 2. Define exchange rates relative to USD (Mapping dictionary)
rates = {'EUR': 0.92, 'SAR': 3.75, 'AED': 3.67}

# 3. Convert amounts to USD Value using Lambda
df['USD_Value'] = df.apply(lambda x: x['Amount'] / rates[x['Currency']], axis=1)

# Display converted transactions
df