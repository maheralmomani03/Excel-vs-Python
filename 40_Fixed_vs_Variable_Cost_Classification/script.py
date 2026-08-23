import pandas as pd

# 1. Load expense description data
df = xl("Cost_Classification_Table[#All]", headers=True)

# 2. Use Lambda logic to classify based on keywords
df['Cost_Type'] = df['Desc'].apply(lambda x: "Fixed" if any(word in x.lower() for word in ['rent', 'lease']) else "Variable")

# Display classified expenses
df