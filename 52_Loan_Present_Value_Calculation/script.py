import pandas as pd

# 1. Load loan data and clean column names
df = xl("Loan_PV[#All]", headers=True)
df.columns = df.columns.str.strip()

# 2. Helper function to handle financial strings (e.g., 500-)
def clean_val(v):
    s = str(v).strip()
    if s.endswith('-'): return -float(s[:-1])
    try: return float(s)
    except: return 0.0

# 3. Mathematical PV Logic (handling monthly rates)
def manual_pv(rate, nper, pmt):
    r = rate / 12
    if r == 0: return -(pmt * nper)
    return pmt * (1 - (1 + r)**-nper) / r * -1

# 4. Apply calculation row-wise
df['Loan_PV'] = df.apply(lambda x: manual_pv(clean_val(x['Rate']), clean_val(x['Nper']), clean_val(x['Pmt'])), axis=1)
df