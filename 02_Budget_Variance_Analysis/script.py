import numpy as np
import pandas as pd

# Load budget and actual data from Excel Table
df = xl("Table2[#All]", headers=True)

# 1. Calculate Variance and Variance Percentage
df['Variance'] = df['Actual'] - df['Budget']
df['Var_%'] = (df['Variance'] / df['Budget']).round(4)

# 2. Automated Status tagging using NumPy
df['Status'] = np.where(df['Variance'] > 0, 'Over Budget ⚠️', 'Within Budget ✅')

# Display final result
df