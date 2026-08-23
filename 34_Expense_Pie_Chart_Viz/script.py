import matplotlib.pyplot as plt
import pandas as pd

# 1. Load expense summary data
df = xl("Expense_Chart_Table[#All]", headers=True)

# 2. Create Pie Chart with percentage labels
plt.pie(df['Amount'], labels=df['Category'], autopct='%1.1f%%')
plt.title("Expense Distribution")

# 3. Show plot
plt.show()