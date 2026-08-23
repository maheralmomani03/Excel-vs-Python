import pandas as pd

# 1. Load historical inflow data
df = xl("Cash_Forecast_Table[#All]", headers=True)

# 2. Calculate 3-Month Moving Average for forecasting
df['Moving_Average'] = df['Inflow'].rolling(window=3).mean()

# Display forecast results
df