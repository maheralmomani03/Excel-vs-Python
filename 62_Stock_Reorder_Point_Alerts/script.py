import pandas as pd

# 1. Load inventory level data
df = xl("Inventory_Alerts[#All]", headers=True)

# 2. Filter products that hit the Minimum Reorder Point
reorder_list = df[df['Stock'] < df['Min_Level']]

# Display items needing immediate purchase
reorder_list