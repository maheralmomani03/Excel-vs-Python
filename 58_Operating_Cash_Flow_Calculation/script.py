import pandas as pd

# 1. Load cash flow components
df = xl("CashFlow_Table[#All]", headers=True)

# 2. Calculate Operating Cash Flow (OCF) using the Indirect Method
# Formula: Net Income + Depreciation - Change in Working Capital
df['OCF'] = df['Net_Income'] + df['Depreciation'] - df['Change_WC']

# Display OCF report
df