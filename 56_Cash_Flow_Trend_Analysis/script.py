import matplotlib.pyplot as plt
import pandas as pd

# 1. Load monthly cash flow data
df = xl("Cash_Flow_Trend[#All]", headers=True)

# 2. Plotting Inflow vs Outflow trends
df.plot(kind='line', x='Month', y=['Inflow', 'Outflow'])
plt.title("Cash Flow Trend Analysis")
plt.ylabel("Amount")

# 3. Show visualization
plt.show()