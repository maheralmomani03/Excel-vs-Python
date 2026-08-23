import pandas as pd
df = xl("String_Table[#All]", headers=True)

# Splitting complex codes (Type-Year-Dept) into separate columns
df[['Type', 'Year', 'Dept']] = df['Code'].str.split('-', expand=True)
df