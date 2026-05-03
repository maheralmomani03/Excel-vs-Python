# 🔗 Day 06: Merging Branch Data (Better than VLOOKUP)
![Cover](../images/11.png)

### 🎯 Objective
Combining multiple related datasets into a single unified table. This process is essential for consolidating data from different branches, inventory lists, or price catalogs without the risk of broken formulas or manual copy-pasting.

### 💼 Accounting Context
* **Data Consolidation:** Merging sales records with pricing masters to generate comprehensive revenue reports.
* **Inventory Valuation:** Linking stock quantities from one system with unit costs from another for accurate balance sheet reporting.
* **Database Management:** Moving away from fragile lookup functions towards robust relational data merging, ensuring better internal control over financial data.

### 📗 Excel Approach
**Formula:**
`=XLOOKUP(Sales_Table[SKU_ID], Prices_Table[SKU_ID], Prices_Table[Price])`

**Logic:**
Searches for the `SKU_ID` in the price master table and returns the corresponding price to the sales table.

### 🐍 Python Approach
**Logic:**
* **`pd.merge()`:** Instead of looking up one value at a time, Python joins the two entire tables based on a common key (`SKU_ID`). This is significantly faster and more auditable for large datasets.
* **Calculation Efficiency:** Once merged, calculating the 'Total' across all records happens in a single vectorized step.

### 📊 Visual Reference
![Formula](../images/12.png)