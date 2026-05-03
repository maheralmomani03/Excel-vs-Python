import pandas as pd

# 1. Load the Aging Table from Excel
df = xl("Aging_Table[#All]", headers=True)

# 2. Clean column names from any hidden spaces
df.columns = df.columns.str.strip()

# 3. Ensure 'Due_Date' is in proper datetime format
df['Due_Date'] = pd.to_datetime(df['Due_Date'], dayfirst=True)

# 4. Calculate days overdue from today
days = (pd.to_datetime('today') - df['Due_Date']).dt.days

# 5. Categorize aging buckets using Bins (pd.cut)
bins = [-999, 0, 30, 60, 999]
labels = ['Current ✅', '1-30 Days ⌛', '31-60 Days ⚠️', '60+ Overdue 🌑']
df['Status'] = pd.cut(days, bins=bins, labels=labels)

# Display specific columns for the final report
df[['Customer', 'Amount', 'Status']]