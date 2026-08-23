import pandas as pd

# 1. Load real-time market data from Excel
df = xl("Gold_Price[#All]", headers=True)

# 2. Extract current value for financial adjustments
current_gold_price = df.iloc[0]['Value']

# Display the market connector result
f"Current Gold Market Price: ${current_gold_price:,.2f}"