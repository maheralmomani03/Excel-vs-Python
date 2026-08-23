import pandas as pd

# 1. Load scenario data from Excel Table
df = xl("Scenario_Table[#All]", headers=True)

# 2. Clean column names to ensure accuracy
df.columns = df.columns.str.strip()

# 3. Calculate Profit Projection based on price change and cost
# Formula: (Qty * (1 + Price_Chg)) * (Price - Cost)
df['Profit_Projection'] = (df['Qty'] * (1 + df['Price_Chg'])) * (df['Price'] - df['Cost'])

# Display final results with new calculations
df