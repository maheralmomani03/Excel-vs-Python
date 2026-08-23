import pandas as pd

# 1. Load data from multiple branch tables
df1 = xl("Branch_A[#All]", headers=True)
df2 = xl("Branch_B[#All]", headers=True)
df3 = xl("Branch_C[#All]", headers=True)

# 2. Consolidate all tables into one Master Table (The pro way)
master_table = pd.concat([df1, df2, df3], ignore_index=True)

# 3. Display the final consolidated report
master_table