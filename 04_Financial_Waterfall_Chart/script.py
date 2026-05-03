import pandas as pd
import matplotlib.pyplot as plt

# 1. Load P&L data from Excel Table
df = xl("PL_Table[#All]", headers=True)

# 2. Define logic for colors (Green for Income, Red for Expenses)
colors = ['green' if x > 0 else 'red' for x in df['Amount']]

# 3. Create the Waterfall Visualization
plt.figure(figsize=(10, 6))
plt.bar(df['Category'], df['Amount'], color=colors)
plt.axhline(0, color='black', linewidth=0.8)
plt.title("Financial Waterfall Analysis")

# 4. Display the chart
plt.show()