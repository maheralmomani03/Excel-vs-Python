# 📈 Day 02: Budget vs Actual Variance Analysis
![Cover](../images/3.png)

### 🎯 Objective
Evaluating financial performance by comparing actual outcomes against predetermined budgets. This analysis highlights operational inefficiencies and helps in monitoring spending across different departments.

### 💼 Accounting Context
* **Management by Exception:** Enables managers to focus solely on significant deviations from the plan, saving time and resources.
* **Operational Control:** Identifies over-spending in real-time to allow for immediate corrective actions.
* **Budget Accuracy:** Provides feedback to improve the accuracy of future financial forecasting and resource allocation.

### 📗 Excel Approach
**Formulas:**
* **Variance:** `=[@Actual]-[@Budget]`
* **Status:** `=IF([@Variance]>0, "Over Budget ⚠️", "Within Budget ✅")`

**Logic:**
Uses standard subtraction and logical IF functions to flag discrepancies between actual and budgeted figures.

### 🐍 Python Approach
**Logic:**
* **Vectorized Subtraction:** Calculates variances for thousands of rows simultaneously without the need for manual formula dragging.
* **`np.where` Logic:** Efficiently assigns a status label based on numerical conditions, which is significantly faster and cleaner for large-scale financial auditing.

### 📊 Visual Reference
![Formula](../images/4.png)