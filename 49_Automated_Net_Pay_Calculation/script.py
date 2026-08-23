import pandas as pd

# 1. Load employee payroll data
df = xl("Payroll_Calculation[#All]", headers=True)

# 2. Calculate Net Pay after Social Security (5%) and Insurance deductions
# Formula: Gross - (Gross * 0.05) - Insurance
df['Net_Pay'] = df['Gross'] - (df['Gross'] * 0.05) - df['Insurance']

# Display final payroll report
df