import pandas as pd

# 1. Load client payment and debt data
df = xl("Credit_Score_Table[#All]", headers=True)

# 2. Calculate Weighted Credit Score
# Weights: 70% Payment History, 30% Outstanding Debt
df['Score'] = (df['History'] * 0.7) + (df['Debt'] * 0.3)

# Display prioritized credit report
df