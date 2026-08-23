import pandas as pd

# 1. Load accounts receivable data
df = xl("AFDA_Table[#All]", headers=True)

# 2. Calculate Required Allowance per bucket
df['Required_AFDA'] = df['Balance'] * df['Provision_Rate']

# 3. Sum the total allowance required for the Balance Sheet
total_provision = df['Required_AFDA'].sum()

# Display final provision amount
f"Total Allowance for Doubtful Accounts: ${total_provision:,.2f}"