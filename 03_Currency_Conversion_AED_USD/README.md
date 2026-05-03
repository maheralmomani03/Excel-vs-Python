# 💱 Day 03: Real-time Currency Conversion (AED to USD)
![Cover](../images/5.png)

### 🎯 Objective
Converting financial transactions from a local functional currency (AED) to a reporting currency (USD). This ensures consistency in global financial reporting and helps in evaluating cross-border transaction values.

### 💼 Accounting Context
* **Foreign Currency Translation:** Essential for businesses operating in multiple jurisdictions to consolidate financial statements.
* **Exchange Rate Precision:** Using standardized rates (like the pegged 3.6725 for AED/USD) ensures accuracy in tax and audit filings.
* **Financial Reporting:** Aligns with international standards regarding the presentation of monetary assets and liabilities in a functional currency.

### 📗 Excel Approach
**Formula:**
`=[@[Amount_AED]] / 3.6725`

**Logic:**
Direct division of the local amount by the exchange rate within an Excel Table to maintain dynamic row updates.

### 🐍 Python Approach
**Logic:**
* **Vectorized Operation:** Performs currency conversion across the entire column instantly, which is highly efficient for high-volume invoice processing.
* **Rounding Precision:** The `.round(2)` function ensures that financial figures meet standard accounting precision requirements.

### 📊 Visual Reference
![Formula](../images/6.png)