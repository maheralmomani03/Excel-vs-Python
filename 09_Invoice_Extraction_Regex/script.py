import pandas as pd
import re

# 1. Load unstructured log data from Excel Table
df = xl("Raw_Log_Table[#All]", headers=True)

# 2. Define Regex function to extract patterns (e.g., INV-xxxx or REF-xxxx)
def extract_inv(text):
    # Matches patterns like INV-9945-AC or REF-873B-P4
    match = re.search(r'(INV|REF)-\w+-\w+|(INV|REF)-\w+', str(text))
    return match.group() if match else "Not Found"

# 3. Apply the extraction logic to the Log_Entry column
df['Invoice_No'] = df['Log_Entry'].apply(extract_inv)

# Display extracted results
df[['Log_Entry', 'Invoice_No']]