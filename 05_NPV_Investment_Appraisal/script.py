import pandas as pd

# 1. Load investment data (Cash flows from Year 0 to Year 5)
df = xl("Investment_Table[#All]", headers=True)

# 2. Define the discount rate (10%)
rate = 0.10

# 3. Generate year indices starting from 0
df['Year_Num'] = range(len(df))

# 4. Calculate Present Value (PV) for each year
# Mathematical Formula: CF / (1 + r)^n
df['PV'] = df['CashFlow'] / (1 + rate)**df['Year_Num']

# 5. Calculate Net Present Value (Total PV Sum) and round to 2 decimals
npv_result = round(df['PV'].sum(), 2)

# Display final result
print(f"Net Present Value (NPV): ${npv_result}")