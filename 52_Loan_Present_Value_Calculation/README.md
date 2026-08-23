# 🏦 Day 52: Loan Present Value (PV) Calculation
![Cover](../images/103.png)

### 🎯 Objective
Calculating the present value of a series of future loan payments to determine the current worth of a debt obligation or investment.

### 💼 Accounting Context
* **Time Value of Money (TVM):** A foundational concept in corporate finance and accounting for long-term liabilities.
* **Debt Valuation:** Determining the fair value of loans or bonds for financial statement disclosure.
* **Audit Verification:** Cross-checking bank-provided amortization schedules.

### 📗 Excel Approach
**Formula:** `=PV(Loan_PV[@Rate]/12, Loan_PV[@Nper], Loan_PV[@Pmt])`

### 🐍 Python Approach
**Logic:** Custom mathematical implementation that provides transparency into the TVM formula ($PV = PMT \times \frac{1 - (1+r)^{-n}}{r}$), while handling messy data inputs like trailing minus signs.

### 📊 Visual Reference
![Formula](../images/104.png)