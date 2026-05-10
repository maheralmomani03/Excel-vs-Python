import pandas as pd
df = xl("OH_Table[#All]", headers=True)
df['Allocated_Cost'] = (df['SqFt'] / df['SqFt'].sum()) * df['Total_Overhead']
df[['Department', 'Allocated_Cost']]