# 💱 Day 47: Automated Multi-Currency Transaction Converter
![Cover](../images/93.png)

### 🎯 Objective
Standardizing transaction amounts from multiple foreign currencies into a single base currency (USD) for consolidated financial reporting.

### 💼 Accounting Context
* **International Reporting:** Essential for companies operating in multiple jurisdictions or dealing with international vendors.
* **Consolidation Accuracy:** Ensuring that all line items are valued using consistent exchange rates before aggregation.
* **Audit Trail:** Provides a clear, programmable logic for how foreign exchange conversions were handled.

### 📗 Excel Approach
**Formula:** `=Transaction_Table[@Amount] / VLOOKUP(Transaction_Table[@Currency], Rates56[#All], 2, 0)`

### 🐍 Python Approach
**Logic:** Using a dictionary-based mapping with `apply(lambda)` for a cleaner and more scalable solution than manual `VLOOKUP` tables.

### 📊 Visual Reference
![Formula](../images/94.png)