import pandas as pd

# 1. Load Sales and Bank data
df_sales = xl("Sales_Data[#All]", headers=True)
df_bank = xl("Bank_Statement[#All]", headers=True)

# 2. Identify invoices in Sales but missing from Bank Statement
missing = df_sales[~df_sales['Inv_ID'].isin(df_bank['Bank_ID'])]

# Display missing invoices for follow-up
missing