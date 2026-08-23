import matplotlib.pyplot as plt
import pandas as pd

# 1. Load marketing and sales data
df = xl("Correlation_Analysis[#All]", headers=True)

# 2. Create a Scatter Plot to visualize the relationship
plt.scatter(df['Ad_Spend'], df['Sales'])
plt.title("Ad Spend vs. Sales Correlation")
plt.xlabel("Advertising Spend")
plt.ylabel("Sales Revenue")

# 3. Show plot
plt.show()