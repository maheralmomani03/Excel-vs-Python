import pandas as pd
import matplotlib.pyplot as plt

# 1. Load distribution data
df = xl("Histogram_Table[#All]", headers=True)

# 2. Create a Histogram to visualize expense distribution
plt.figure(figsize=(8, 6))
plt.hist(df['Amount'], bins=5, color='skyblue', edgecolor='black')
plt.title("Expense Distribution Analysis")
plt.xlabel("Amount Range")
plt.ylabel("Frequency")

# 3. Show the plot
plt.show()