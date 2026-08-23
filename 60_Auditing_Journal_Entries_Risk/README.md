# 🕵️‍♂️ Day 60: Auditing Manual Journal Entries for Risks
![Cover](../images/119.png)

### 🎯 Objective
Automating audit procedures to identify manual journal entries, which are statistically higher-risk areas for human error or management override of controls.

### 💼 Accounting Context
* **Internal Control:** Monitoring the segregation of duties and adherence to journal approval policies.
* **Fraud Risk:** Manual entries are often scrutinized by external auditors as a prime area for potential financial statement manipulation.
* **Audit Efficiency:** Instantly isolating manual transactions from millions of automated system entries.

### 📗 Excel Approach
**Formula:**
`=FILTER(GL_Entries, GL_Entries[Source]="Manual")`

### 🐍 Python Approach
**Logic:**
Using fast boolean indexing to filter through massive ledger exports, enabling proactive, real-time audit monitoring.

### 📊 Visual Reference
![Formula](../images/120.png)