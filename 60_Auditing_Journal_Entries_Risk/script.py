import pandas as pd

# 1. Load General Ledger entries
df = xl("GL_Entries[#All]", headers=True)

# 2. Filter for Manual Entries (High Risk Audit Flag)
manual_entries = df[df['Source'] == 'Manual']

# Display high-risk entries for audit testing
manual_entries