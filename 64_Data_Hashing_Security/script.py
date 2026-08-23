import pandas as pd
import hashlib

# 1. Load sensitive financial data
df = xl("Bank_Account[#All]", headers=True)

# 2. Irreversible Hashing (SHA-256) for account numbers
# This ensures that even if data is leaked, original numbers remain secret
df['Hashed_Acc'] = df['Acc_Number'].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())

# Display secured data for internal auditing
df[['Hashed_Acc']]