# 📉 Automated Stocktake Variance Reporter (Retail Ops)

> **A Python-based automation tool designed to turn messy SAP Variance Reports into actionable insights in seconds.**

![Logic Tests](https://github.com/Lwg78/Stocktake-Variance-Reporter/actions/workflows/run_tests.yml/badge.svg)
![Demo Pipeline](https://github.com/Lwg78/Stocktake-Variance-Reporter/actions/workflows/run_demo.yml/badge.svg)

## 📌 Executive Summary
**Problem:** Retail Store Managers (e.g., at NTUC FairPrice) spend hours after every stocktake manually filtering raw SAP Excel dumps. They have to separate thousands of SKUs into classes (Fresh vs. Grocery), calculate variances, and manually identify top losses.

**Solution:** This tool automates the entire workflow. It ingests the raw SAP file, cleans the data, sorts it into departmental tabs, and uses a **Rule-Based AI Engine** to flag potential theft, receiving errors, or contra items automatically.

---

## 📸 Demo Output (Privacy Safe)

### 1. The Clean Report Structure
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

**No coding skills required.** You have two ways to run this tool.

### Option A: The "One-Click" Method (Standard)
1.  **Download from SAP:** Export your standard Stocktake Variance Report (e.g., `HGPT Mid Year.xlsx`).
2.  **Drop the File:** Place your Excel file into the `input/` folder.
3.  **Run:** Double-click `run.bat` (Windows).
4.  **Result:** Check the `output/` folder for your processed `Report_....xlsx`.

### Option B: The Web Interface (Modern)
Prefer a drag-and-drop website?
1.  **Start the App:** Double-click `start_server.bat` (See "Installation" below to create this).
2.  **Open Browser:** Go to `http://127.0.0.1:8000`
3.  **Upload & Download:** Drag your file onto the page and get the report instantly.

---

# 💻 Developer Guide: For AISG & Engineers

### 🔒 Data Privacy & Mock Data (Security First)
**NOTE:** To comply with data privacy policies, **NO REAL INTERNAL DATA** is hosted in this repository.
* **`.gitignore` Policy:** All `.xls/.xlsx` files are strictly ignored.
* **Mock Data Generator:** Use `src/mock_data_gen.py` to generate realistic "Fake SAP Data" for testing.

### 🛠 Architecture
```text
stocktake-variance-reporter/
├── input/                  # 📂 Input Zone (Git-ignored)
├── output/                 # 📂 Output Zone (Git-ignored)
├── src/
│   ├── processor.py        # ⚙️ ETL Logic (Cleaning, Tab Separation)
│   ├── remarks_engine.py   # 🤖 Logic Unit (The "AI" findings generator)
│   ├── config.py           # 🧠 Domain Knowledge (Class Codes)
│   └── mock_data_gen.py    # 🧪 Test Data Generator
├── tests/
│   └── test_remarks.py     # ✅ Unit Tests for Business Logic
├── static/
│   └── index.html          # 🌐 Frontend (Simple HTML/JS Dashboard)
├── .github/workflows/      # 🤖 CI/CD Pipeline (Runs tests & demo)
├── api.py                  # 🔌 Backend API (FastAPI)
├── Dockerfile              # 🐳 Container Configuration
├── main.py                 # 🚀 CLI Entry Point
└── requirements.txt        # Dependencies
```

### ✅ Quality Assurance (CI/CD)
This repository uses **GitHub Actions** to automatically test the business logic on every commit.
* **Test Suite:** `tests/test_remarks.py`
* **Coverage:** Verifies that the AI Engine correctly flags Contra Items (`DA - Item`), High Value Theft (`>$500`), and UOM Errors.

### 🐳 Deployment (Docker)
To run this in a containerized environment (ensuring it runs on any OS):
```bash
docker build -t stocktake-tool .
docker run -p 8000:8000 stocktake-tool
```

---

## ⚙️ Installation (Windows Setup for Managers)
If setting this up on a Store Laptop for the first time:

1.  **Install Python:**
    * Download Python 3.9+ from [python.org](https://www.python.org/downloads/).
    * **CRITICAL:** Check the box that says **"Add Python to PATH"** during installation.

2.  **Install Libraries (One-Time Setup):**
    * Double-click the file `install_deps.bat` included in this folder.
    * Wait for the "Installation Complete" message.

3.  **Launch the App:**
    * **Option A (Standard):** Double-click `run.bat` to process files instantly.
    * **Option B (Web Mode):** Double-click `start_server.bat` to open the website interface.

---

## 📜 Disclaimer
This is a personal project developed by Lim Wen Gio based on operational experience in the FMCG sector. It is **not** an official software product of NTUC FairPrice Co-operative Ltd.
