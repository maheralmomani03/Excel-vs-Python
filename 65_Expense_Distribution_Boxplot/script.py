import matplotlib.pyplot as plt
import pandas as pd

# 1. Load expense distribution data
df = xl("Expense_Dist_Table[#All]", headers=True)

# 2. Create Boxplot to analyze expense spread by Branch
df.boxplot(column='Expenses', by='Branch')
plt.title("Expense Distribution by Branch")
plt.suptitle("") # Remove default title

# 3. Show visualization
plt.show()