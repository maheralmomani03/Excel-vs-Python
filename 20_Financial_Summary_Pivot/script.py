import pandas as pd
df = xl("Expense_Table[#All]", headers=True)

# Instant summary using multi-aggregation (Pivot logic)
summary = df.groupby('Category')['Amount'].agg(['sum', 'mean', 'count'])
summary