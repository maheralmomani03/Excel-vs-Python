import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load correlation data
df = xl("Correlation_Table[#All]", headers=True)
df.columns = df.columns.str.strip()

# 2. Generate Heatmap to visualize relationships
plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='RdYlGn')
plt.title("Expense Categories Correlation")
plt.show()