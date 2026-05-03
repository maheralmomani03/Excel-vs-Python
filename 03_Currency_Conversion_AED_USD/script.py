import pandas as pd

# 1. Load invoice data from Excel Table
df = xl("Invoices_Table[#All]", headers=True)

# 2. Convert AED to USD using a fixed rate (3.6725) and round to 2 decimals
df['Amount_USD'] = (df['Amount_AED'] / 3.6725).round(2)

# 3. Display only the converted column or the whole dataframe
df[['Invoice_No', 'Amount_AED', 'Amount_USD']]