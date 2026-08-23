import pandas as pd

# 1. Load financial and HR metrics
df = xl("Revenue_Metrics[#All]", headers=True)

# 2. Calculate Revenue per Employee Ratio
df['Rev_per_Emp'] = df['Total_Rev'] / df['Employee_Count']

# Display productivity report
df