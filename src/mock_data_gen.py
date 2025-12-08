import pandas as pd
import numpy as np
import os

# Define where to save the fake file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_PATH = os.path.join(BASE_DIR, 'input', 'MOCK_SAP_REPORT.xlsx')

def create_mock_report():
    print("🧪 Generating MOCK Stocktake Data...")
    
    # 1. Create Fake Data Dictionary
    data = {
        'Material': np.random.randint(1000000, 9999999, 50),
        'Article Description': [
            'FRESH PORK RIB', 'DA - FROZEN WINGS', 'SADIA WINGS NEW', 'BRANDY VSOP', 
            'MILK POWDER 900G', 'HABA SHAMPOO', 'RICE 5KG', 'CANNED TUNA', 
            'UNKNOWN ITEM', 'FRESH EGGS 30S'
        ] * 5,
        'Matl Group': [
            '21050', '21040', '21040', '21010', 
            '21018', '21081', '21010', '21012', 
            '21099', '21052'
        ] * 5,
        'Plant': ['Supermarket'] * 50,
        'Storage Loc': ['0001'] * 50,
        # Random Variance Logic
        'Quantity Variance': np.random.randint(-20, 20, 50),
    }
    
    df = pd.DataFrame(data)
    
    # 2. Add Business Logic (Value = Qty * Random Cost)
    df['Value Variance'] = df['Quantity Variance'] * np.random.uniform(5.0, 150.0, 50)
    
    # 3. Inject Specific "Test Cases" for your Remarks Engine
    # Case A: Massive Theft (High Value Loss)
    df.loc[0, 'Value Variance'] = -600 
    df.loc[0, 'Article Description'] = 'EXPENSIVE BRANDY'
    
    # Case B: Contra Item
    df.loc[1, 'Article Description'] = 'DA - OLD PACKING'
    df.loc[1, 'Value Variance'] = -100
    df.loc[2, 'Article Description'] = 'NEW PACKING'
    df.loc[2, 'Value Variance'] = 100
    
    # 4. Save to Input Folder (mimicking a SAP dump)
    # We add 11 empty rows at the top to simulate the "messy" SAP format
    with pd.ExcelWriter(OUTPUT_PATH, engine='openpyxl') as writer:
        pd.DataFrame(["SAP REPORT HEADER"]*5).to_excel(writer, startrow=0, index=False, header=False)
        df.to_excel(writer, startrow=11, index=False)
        
    print(f"✅ MOCK file created at: {OUTPUT_PATH}")
    print("   -> Run 'main.py' now to test the reporter!")

if __name__ == "__main__":
    create_mock_report()