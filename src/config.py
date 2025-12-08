# src/config.py

# ==========================================
# MASTER CLASS MAPPING (Supermarket Standard)
# ==========================================
# Map the last 2 digits of 'Matl Group' to Department Names
CLASS_MAPPING = {
    # --- DEPT 1: GROCERY (Dry Food) ---
    '10': 'Grocery - Rice & Oil',
    '11': 'Grocery - Sauces & Condiments',
    '12': 'Groocery - Canned Food',
    '13': 'Groocery - Beverages & Water',
    '14': 'Groocery - Hot Beverages (Coffee/Tea)',
    '15': 'Groocery - Biscuits & Snacks',
    '16': 'Groocery - Confectionery',
    '17': 'Groocery - Breakfast & Baking',
    '18': 'Groocery - Baby Food',
    '19': 'Groocery - Ethnic/Specialty',
    
    # --- DEPT 2: GROCERY (Non-Food) ---
    '20': 'Groocery - Household Cleaning',
    '21': 'Groocery - Paper Products',
    '22': 'Groocery - Laundry',
    '23': 'Groocery - Pet Food',
    '24': 'Groocery - Insecticides/Air Care',
    
    # --- DEPT 3: FRESH & FROZEN  ---
    '40': 'Fresh General',
    '43': 'F&D - Dairy Spread',
    '44': 'F&D - Chilled Juice',
    '45': 'F&D - Milk/Soya',
    '46': 'F&D - Frozen Poultry',
    '47': 'F&D - Frozen Processed',
    '48': 'F&D - Frozen Snacks',
    '49': 'F&D - Ice Cream',
    '50': 'Fresh - Pork',
    '51': 'Fresh - Seafood',
    '52': 'Fresh - Eggs',
    '53': 'Fresh - Poultry',
    '54': 'Fresh - Beef',
    '55': 'Fresh - Prepack',
    '56': 'Fresh - Delicatessen',
    '57': 'Fresh - Temperate Fruits',
    '58': 'Fresh - Excotic Fruits',
    '59': 'Fresh - Tropical Fruits',
    '60': 'Fresh - Vegetables',
    '61': 'Fresh - Bread',
    
    # --- DEPT 4: HABA (Health & Beauty) ---
    '80': 'HABA - Personal Care (Soap/Body)',
    '81': 'HABA - Hair Care',
    '82': 'HABA - Oral Care',
    '83': 'HABA - Feminine Care',
    '84': 'HABA - Baby Care (Diapers)',
    '85': 'HABA - Cosmetics',
    '86': 'HABA - Pharmacy/Health',

    # --- DEPT 5: GENERAL MERCHANDISE (GM) ---
    '90': 'GM - Electrical',
    '91': 'GM - Hardware/DIY',
    '92': 'GM - Stationery',
    '93': 'GM - Textile/Apparel',
    '94': 'GM - Footwear',
    '95': 'GM - Toys',
    '99': 'GM - Miscellaneous',
    # Add more as needed based on your experience
    # Add generic mapping just in case
    '00': 'Unknown'
}

# Columns we expect from SAP (Normalized)
# UPDATE THIS BLOCK
EXPECTED_COLS = {
    # 'Column Name in Excel': 'Name our Script Needs'
    'sku': 'sku',                         # It seems your file already calls it 'sku'
    'Article': 'sku',                     # Keeping this just in case other files use 'Article'
    'Article Description': 'description',
    'Class': 'class_code',                # Matches your file's "Class" column
    'Matl Group': 'class_code',           # Keeping for compatibility with other formats
    'Quantity Variance': 'qty_diff',      # Your file uses "Variance"
    'Difference Quantity': 'qty_diff',    # Other files might use "Difference"
    'Value Variance': 'val_diff',         # Your file uses "Value Variance"
    'Value of Difference': 'val_diff'     # Other files might use "Value of Difference"
}