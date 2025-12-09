# 📉 Automated Stocktake Variance Reporter (Retail Ops)

> **A Python-based automation tool designed to turn messy SAP Variance Reports into actionable insights in seconds.**

![Logic Tests](https://github.com/Lwg78/Stocktake-Variance-Reporter/actions/workflows/run_tests.yml/badge.svg)
![Demo Pipeline](https://github.com/Lwg78/Stocktake-Variance-Reporter/actions/workflows/run_demo.yml/badge.svg)

## 📌 Executive Summary
**Problem:** Retail Store Managers (e.g., at NTUC FairPrice) spend hours after every stocktake manually filtering raw SAP Excel dumps. They have to separate thousands of SKUs into classes (Fresh vs. Grocery), calculate variances, and manually identify top losses.

**Solution:** This tool automates the entire workflow. It ingests the raw SAP file, cleans the data, sorts it into departmental tabs, and uses a **Rule-Based AI Engine** to flag potential theft, receiving errors, or contra items automatically.


--- 

## 📸 Demo Output (Privacy Safe)

### 1. The Terminal Output
When you run the script, you will see a clean execution log confirming the automatic sorting logic:

```text
🚀 STARTING STOCKTAKE VARIANCE REPORTER
=======================================
📂 Scanning folder: /root/stocktake-variance-reporter/input/
🔎 Found 1 files to process...

📂 Processing: MOCK_SAP_REPORT.xlsx
   ✅ Tab Created: 50 - Fresh Pork (Top 10 Gains/Losses)
   ✅ Tab Created: 81 - HABA Hair Care (Top 10 Gains/Losses)
   ✅ Tab Created: 43 - Dairy Spread (Top 10 Gains/Losses)
   
🤖 Remarks Engine Findings:
   -> Flagged 2 "Contra" items (Packaging Change)
   -> Flagged 1 High Value Loss ($600+)
   
🎉 Report Generated: /root/stocktake-variance-reporter/output/Report_MOCK_SAP_REPORT.xlsx
```

### 2. The Clean Report Structure
The tool transforms the raw SAP dump into organized tabs. Here is a preview of the generated data structure:

**Tab: 50 - Fresh Pork**

| SKU | Description | Qty Variance | Val Variance | Remarks (Auto-Generated) |
| :--- | :--- | :--- | :--- | :--- |
| **Gains** | | | | |
| 10293 | SADIA WINGS NEW | +10 | +$100.00 | |
| 59201 | PORK RIB PREM | +5 | +$45.00 | |
| **Losses** | | | | |
| 10292 | DA - SADIA WINGS | -10 | -$100.00 | **⚠️ Contra/Pkg Change?** |
| 88210 | EXPENSIVE BRANDY | -1 | -$600.00 | **📉 High Value LOSS ($600) - Investigate Theft** |


---

# 🛍️ User Guide: For Store Managers

**No coding skills required.** If you can use Excel, you can use this tool.

### 🚀 How to Generate Your Report
1.  **Download from SAP:** Export your standard Stocktake Variance Report (e.g., `HGPT Mid Year.xlsx`).
2.  **Drop the File:** Place your Excel file into the `input/` folder.
3.  **Run the Reporter:** Double-click `run.bat` (Windows) or run the script.
4.  **Open Results:** Check the `output/` folder for your processed `Report_....xlsx`.

### 📊 What You Will See
* **Summary Tab:** Total $ Variance by Department.
* **Department Tabs:** (e.g., `50 - Fresh Pork`)
    * **Top 10 Gains:** Listed at the top.
    * **Top 10 Losses:** Listed at the bottom.
* **"Remarks" Column:** Auto-filled suggestions:
    * *Example:* `⚠️ Contra/Pkg Change?` (For "DA" items)
    * *Example:* `📉 High Value LOSS ($600)` (For theft investigation)

---

# 💻 Developer Guide: For AISG & Engineers

### 🔒 Data Privacy & Mock Data (Security First)
**NOTE:** To comply with data privacy policies, **NO REAL INTERNAL DATA** is hosted in this repository.
* **`.gitignore` Policy:** All `.xls/.xlsx` files are strictly ignored.
* **Mock Data Generator:** I have included `src/mock_data_gen.py` which generates a realistic "Fake SAP Report" so you can test the pipeline's logic without accessing sensitive corporate data.

### 🛠 Architecture
```text
stocktake-variance-reporter/
├── input/                  # 📂 Input Zone (Git-ignored)
├── output/                 # 📂 Output Zone (Git-ignored)
├── src/
│   ├── config.py           # 🧠 Domain Knowledge (Class Codes: 50=Pork, 81=HABA)
│   ├── processor.py        # ⚙️ ETL Logic (Cleaning, Tab Separation)
│   ├── remarks_engine.py   # 🤖 Logic Unit (The "AI" findings generator)
│   └── mock_data_gen.py    # 🧪 Test Data Generator
├── tests/
│   └── test_remarks.py     # ✅ Unit Tests for Business Logic
├── .github/workflows/      # 🤖 CI/CD Pipeline (Runs tests & demo)
├── main.py                 # 🚀 Entry Point
└── requirements.txt        # Dependencies
```
### ✅ Quality Assurance (CI/CD)
This repository uses GitHub Actions to automatically test the business logic on every commit.

* **Test Suite:** `tests/test_remarks.py`

* **Coverage:** Verifies that the AI Engine correctly flags Contra Items (`DA - Item`), High Value Theft (`>$500`), and UOM Errors.

### ☁️ Live Cloud Demo
You don't need to clone the code to see it work.

* Go to the **Actions** tab.

* Click **Run Stocktake Demo**.

* Scroll down to **Artifacts** to download the Excel report generated by this code in the cloud.

## 📜 Disclaimer
This is a personal project developed by Lim Wen Gio based on operational experience in the FMCG sector. It is not an official software product of NTUC FairPrice Co-operative Ltd.
