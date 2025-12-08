import pandas as pd
import os
import re  # <--- NEW: For cleaning illegal characters
from src.config import CLASS_MAPPING, EXPECTED_COLS
from src.remarks_engine import generate_auto_remark

def clean_column_names(df):
    df.columns = [str(c).strip() for c in df.columns]
    df.rename(columns=EXPECTED_COLS, inplace=True)
    return df

def robust_class_extractor(val):
    """
    Handles messy inputs like 50, 50.0, '21050', '50 ' to extract '50'.
    """
    try:
        s = str(val).strip()
        if s.lower() == 'nan': return None
        if '.' in s: s = s.split('.')[0]
        return s[-2:].zfill(2)
    except:
        return None

def process_stocktake_file(filepath, output_path):
    print(f"📂 Processing: {os.path.basename(filepath)}")
    
    try:
        # Read file (try standard first, then skip rows if needed)
        df = pd.read_excel(filepath)
        if 'Class' not in df.columns and 'Article' not in df.columns:
            df = pd.read_excel(filepath, header=11)
            
        df = clean_column_names(df)
        
        # Validate critical columns
        required = ['class_code', 'val_diff', 'qty_diff', 'description']
        if not all(col in df.columns for col in required):
            print(f"⚠️ Missing columns in {os.path.basename(filepath)}. Columns found: {df.columns.tolist()}")
            return

        # 1. Robust Class ID Extraction
        df['class_id'] = df['class_code'].apply(robust_class_extractor)
        df = df.dropna(subset=['class_id'])

        # 2. Generate Remarks
        df['Remarks'] = df.apply(generate_auto_remark, axis=1)

        # 3. Create Excel Report
        with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
            
            # --- TAB 1: SUMMARY ---
            summary = df.groupby('class_id')['val_diff'].sum().reset_index()
            summary['Dept_Name'] = summary['class_id'].map(CLASS_MAPPING)
            summary.to_excel(writer, sheet_name='Summary', index=False)
            
            # --- TAB 2+: CLASS TABS ---
            unique_classes = sorted(df['class_id'].unique())
            
            for cls in unique_classes:
                if not cls or cls == 'an': continue

                class_name = CLASS_MAPPING.get(cls, f"Class {cls}")
                
                # --- NEW: SANITIZE SHEET NAME ---
                raw_sheet_name = f"{cls} - {class_name}"
                # Replace illegal chars (\ / ? * [ ] :) with an underscore
                clean_name = re.sub(r'[\\/*?:\[\]]', '_', raw_sheet_name)
                # Truncate to 30 chars (Excel limit is 31)
                sheet_name = clean_name[:30]
                
                subset = df[df['class_id'] == cls].copy()
                
                # 4. Top 10 Gains & Losses Logic
                # Sort descending to find Gains
                subset_sorted = subset.sort_values(by='val_diff', ascending=False)
                
                top_gains = subset_sorted[subset_sorted['val_diff'] > 0].head(10)
                
                # Sort ascending to find largest LOSSES (most negative numbers)
                top_losses = subset.sort_values(by='val_diff', ascending=True)
                top_losses = top_losses[top_losses['val_diff'] < 0].head(10)
                
                # Spacer row for readability
                spacer = pd.DataFrame([{'description': '--- TOP 10 LOSSES BELOW ---'}])
                
                # Combine: Gains -> Spacer -> Losses
                final_view = pd.concat([top_gains, spacer, top_losses], ignore_index=True)
                
                # Write to tab
                final_view.to_excel(writer, sheet_name=sheet_name, index=False)
                print(f"   ✅ Tab Created: {sheet_name}")

        print(f"🎉 Report Generated: {output_path}")

    except Exception as e:
        print(f"❌ Critical Error in {os.path.basename(filepath)}: {e}")