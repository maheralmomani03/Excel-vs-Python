import pandas as pd
df = xl("Audit_Table[#All]", headers=True)
duplicates = df[df.duplicated(subset=['Date', 'Amount'], keep=False)]
duplicates