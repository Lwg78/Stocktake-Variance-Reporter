import os
import glob
from src.processor import process_stocktake_file

# --- THE FIX: DYNAMIC ABSOLUTE PATHS ---
# Get the directory where THIS script (main.py) lives
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build paths relative to main.py
INPUT_DIR = os.path.join(BASE_DIR, 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'output')

def main():
    print("🚀 STARTING STOCKTAKE VARIANCE REPORTER")
    print(f"📂 Scanning folder: {INPUT_DIR}")  # Debug print to see where it's looking
    
    # Check if input folder exists
    if not os.path.exists(INPUT_DIR):
        print(f"❌ CRITICAL ERROR: Input folder not found at: {INPUT_DIR}")
        print("   -> Did you create the 'input' folder inside 'stocktake-variance-reporter'?")
        return

    # Find all Excel files
    # Get all files and filter by extension in a case-insensitive way
    all_files_in_dir = glob.glob(os.path.join(INPUT_DIR, '*'))
    excel_extensions = ('.xls', '.xlsx')
    files = [f for f in all_files_in_dir if f.lower().endswith(excel_extensions)]
    
    # Filter out temporary Excel files (start with ~$)
    files = [f for f in files if not os.path.basename(f).startswith('~')]
    
    if not files:
        print("⚠️ No Excel files found!")
        print(f"   -> Please drop your .xls/.xlsx files here: {INPUT_DIR}")
        return

    print(f"🔎 Found {len(files)} files to process...")

    # Ensure output folder exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for file in files:
        filename = os.path.basename(file).split('.')[0]
        output_file = os.path.join(OUTPUT_DIR, f"Report_{filename}.xlsx")
        
        process_stocktake_file(file, output_file)

if __name__ == "__main__":
    main()