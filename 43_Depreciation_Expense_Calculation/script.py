import pandas as pd

# 1. Load fixed assets data
df = xl("Depreciation_Table[#All]", headers=True)

# 2. Calculate Straight-Line Depreciation
# Formula: (Cost - Salvage) / Life
df['Yearly_Depr'] = (df['Cost'] - df['Salvage']) / df['Life']

# Display updated asset register
df