import pandas as pd

# 1. Load sensitive account data from Excel Table
df = xl("Account_Table[#All]", headers=True)

# 2. Masking logic: keep only the last 4 digits for security (GDPR/Compliance)
df['Masked'] = df['Acc_Number'].apply(lambda x: '****' + str(x)[-4:])

# Display masked results
df[['Acc_Number', 'Masked']]