# 🔍 Day 09: Extracting Invoice Numbers from Raw Text
![Cover](../images/17.png)

### 🎯 Objective
Automating the extraction of structured identifiers (Invoice or Reference numbers) from unstructured text strings. This is a common challenge when processing bank statement descriptions or manual journal entry memos.

### 💼 Accounting Context
* **Bank Reconciliation:** Quickly identifying invoice numbers within bank transaction descriptions to match them with accounts receivable.
* **Audit Procedures:** Systematically extracting reference codes from large volumes of ledger comments to verify transaction support.
* **Data Cleaning:** Transforming "dirty" text logs into structured data fields ready for analysis and reporting.

### 📗 Excel Approach
**Formula:**
`=IFERROR(MID(A2, SEARCH("INV-", A2), 11), IFERROR(MID(A2, SEARCH("REF-", A2), 11), "Not Found"))`

**Logic:**
Uses nested `IFERROR` with `MID` and `SEARCH` to find specific keywords. However, this approach is "fragile" because it requires fixed lengths and fails if the pattern format changes slightly.

### 🐍 Python Approach
**Logic:**
* **Regular Expressions (RegEx):** Uses the `re` library to define a flexible pattern `(INV|REF)-\w+`. This looks for either "INV" or "REF" followed by a hyphen and any sequence of characters.
* **Pattern Matching:** Python can handle multiple different invoice formats in a single pass, making it much more robust than nested Excel formulas.
* **Scalability:** Processes thousands of rows of messy text logs in seconds with 100% accuracy.

### 📊 Visual Reference
![Formula](../images/18.png)