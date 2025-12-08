# 📉 Automated Stocktake Variance Reporter (Retail Ops)

> **A Python-based automation tool designed to turn messy SAP Variance Reports into actionable insights in seconds.**

## 📌 Executive Summary
**Problem:** Retail Store Managers (e.g., at NTUC FairPrice) spend hours after every stocktake manually filtering raw SAP Excel dumps. They have to separate thousands of SKUs into classes (Fresh vs. Grocery), calculate variances, and manually identify top losses.

**Solution:** This tool automates the entire workflow. It ingests the raw SAP file, cleans the data, sorts it into departmental tabs, and uses a **Rule-Based AI Engine** to flag potential theft, receiving errors, or contra items automatically.

---

# 🛍️ User Guide: For Store Managers

**No coding skills required.** If you can use Excel, you can use this tool.

### 🚀 How to Generate Your Report (3 Steps)

1.  **Download from SAP:**
    * Export your standard Stocktake Variance Report (e.g., `Mid Year Stocktake.xlsx`).
    * **Do not modify the file.** The tool handles the messy headers for you.
2.  **Drop the File:**
    * Place your Excel file into the `input/` folder of this tool.
3.  **Run the Reporter:**
    * Double-click the `run.bat` (Windows) or run the script.
    * *Wait 5-10 seconds...*
4.  **Open Results:**
    * Go to the `output/` folder.
    * Open the new `Report_....xlsx` file.

### 📊 What You Will See
Your new Excel file will be organized cleanly:
* **Summary Tab:** Total $ Variance by Department (know where you stand instantly).
* **Department Tabs:** (e.g., `50 - Fresh Pork`, `81 - Hair Care`)
    * **Top 10 Gains:** Listed at the top (Check for receiving errors).
    * **Top 10 Losses:** Listed at the bottom (Check for shrinkage/theft).
* **"Remarks" Column:** The tool automatically fills this in for you!
    * *Example:* `⚠️ Contra/Pkg Change?` (For "DA" items)
    * *Example:* `📉 High Value LOSS ($600)` (For theft investigation)

> **💡 Need Installation Help?**
> Since this tool runs on Python, it may need to be set up on your Manager Laptop or Store Intranet PC.
> **Contact me directly (Wen Gio)**. I can assist with:
> * Installing the portable version on Windows (no Admin rights needed).
> * Configuring the tool for your specific store layout.

---

# 💻 Developer Guide: For AISG & Engineers

**Context:** This project demonstrates **Domain-Driven Design**. It translates specific Retail Operations logic into a modular, maintainable Python pipeline.

### 🔒 Data Privacy & Mock Data (Security First)
**NOTE:** To comply with data privacy policies, **NO REAL INTERNAL DATA** is hosted in this repository.
* **`.gitignore` Policy:** All `.xls/.xlsx` files are strictly ignored.
* **Mock Data Generator:** I have included `src/mock_data_gen.py` which generates a realistic "Fake SAP Report" so you can test the pipeline's logic without accessing sensitive corporate data.

### 🛠 Architecture
The system uses a modular "Processor-Engine" architecture:

```text
stocktake-variance-reporter/
├── input/                  # 📂 Input Zone (Git-ignored for security)
├── output/                 # 📂 Output Zone (Git-ignored)
├── src/
│   ├── config.py           # 🧠 Domain Knowledge (Class Codes: 50=Pork, 81=HABA)
│   ├── processor.py        # ⚙️ ETL Logic (Cleaning, Tab Separation, Excel Formatting)
│   ├── remarks_engine.py   # 🤖 Logic Unit (The "AI" that suggests findings)
│   └── mock_data_gen.py    # 🧪 Test Data Generator
├── main.py                 # 🚀 Entry Point
└── requirements.txt        # Dependencies (pandas, openpyxl)
```
## 🧠 Key Engineering Challenges Solved
* **Robust Ingestion:** SAP reports often have variable header rows (sometimes row 0, sometimes row 11). processor.py implements a "hunting" algorithm to find the true header dynamically.

* **Sanitization:** Class names like "Fruits/Veg" cause Excel crashes (illegal characters in sheet names). The pipeline automatically sanitizes these to Fruits_Veg using Regex.

* **Extensible Logic:** The remarks_engine.py uses a Registry Pattern. New logic (e.g., "Check for Promo Items") can be added as a standalone function and registered in ACTIVE_RULES without touching the main codebase.

## 🧪 How to Test (Developer Mode)
Clone the repo.

Install dependencies: 
```
pip install -r requirements.txt
```

Generate Test Data:
Bash
```
python src/mock_data_gen.py
```
(This creates a dummy MOCK_SAP_REPORT.xlsx in the input folder)

Run the Pipeline:
Bash
```
python main.py
```

Check output/ for the generated report.

## 📜 Disclaimer
This is a personal project developed by Lim Wen Gio based on operational experience in the FMCG sector. It is not an official software product of NTUC FairPrice Co-operative Ltd.