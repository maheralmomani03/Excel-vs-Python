import pandas as pd
from scipy.optimize import fsolve

# 1. سحب البيانات من جدول إكسيل
df = xl("IRR_Table[#All]", headers=True)

# 2. تنظيف أسماء الأعمدة من أي مسافات مخفية (حل مشكلة KeyError)
df.columns = df.columns.str.strip()

# 3. دالة ذكية لتنظيف الأرقام (تحول 100000- إلى رقم سالب حقيقي)
def clean_val(v):
    s = str(v).strip()
    if s.endswith('-'): return -float(s[:-1])
    try: return float(s.replace(',', ''))
    except: return 0.0

# نطبق التنظيف على أول عمود في الجدول تلقائياً
col_name = df.columns[0]
cash_flows = [clean_val(x) for x in df[col_name]]

# 4. دالة حساب الـ IRR
def npv_func(r):
    return sum(cf / (1 + r)**t for t, cf in enumerate(cash_flows))

# البحث عن النتيجة (البدء بتقدير 10%)
irr_result = fsolve(npv_func, 0.1)[0]

# عرض النتيجة النهائية
f"The Internal Rate of Return (IRR) is: {irr_result:.2%}"