import pandas as pd

# 1. Load bank log data from Excel Table
df = xl("Bank_Log_Table[#All]", headers=True)

# 2. Extract dates using Regular Expressions (DD/MM/YYYY pattern)
# This looks for: 2 digits + / + 2 digits + / + 4 digits
df['Extracted_Date'] = df['Desc'].str.extract(r'(\d{2}/\d{2}/\d{4})')

# Display result
df