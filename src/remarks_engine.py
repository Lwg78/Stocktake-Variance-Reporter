# src/remarks_engine.py

"""
REMARKS ENGINE
==============
This module contains the logic for auto-generating stocktake findings.
To add a new rule, define a function that takes a 'row' and returns a string (or None).
Then, add that function to the RULE_REGISTRY list at the bottom.
"""

# --- RULE DEFINITIONS ---

def check_contra_items(row):
    """
    Detects potential packaging changes or contra items.
    Logic: Description starts with 'DA', 'D-', or 'D '.
    """
    desc = str(row['description']).upper().strip()
    if desc.startswith("DA ") or desc.startswith("D-") or desc.startswith("D -"):
        return "⚠️ Contra/Pkg Change? (Check for New SKU match)"
    return None

def check_high_value_loss(row):
    """
    Flags significant monetary LOSS (> $500).
    Context: Theft, Shrinkage, or missed credit note.
    """
    if row['val_diff'] < -500:
        return f"📉 High Value LOSS ({'$' + str(int(row['val_diff']))}) - Investigate Theft/Shrinkage"
    return None

def check_high_value_gain(row):
    """
    Flags significant monetary GAIN (> $500).
    Context: Receiving error (supplier sent extra) or wrong stock adjustment.
    """
    if row['val_diff'] > 500:
        return f"📈 High Value GAIN ({'$' + str(int(row['val_diff']))}) - Check Invoices/Receiving"
    return None

def check_high_qty_loss(row):
    """
    Flags massive quantity disappearance (> 50 units).
    Context: 'Carton vs Unit' error? (e.g., counted 1 carton but system thought 1 unit?)
    """
    if row['qty_diff'] <= -50:
        return f"📦 High Qty LOSS ({int(row['qty_diff'])} units) - Check UOM / Carton Count?"
    return None

def check_high_qty_gain(row):
    """
    Flags massive quantity appearance (> 50 units).
    Context: Missed counting during LAST stocktake?
    """
    if row['qty_diff'] >= 50:
        return f"📦 High Qty GAIN ({int(row['qty_diff'])} units) - Missed count last time?"
    return None

def check_controlled_items(row):
    """
    Flags sensitive items (Liquor, Tobacco, Milk Powder) that require double-counting.
    """
    desc = str(row['description']).upper()
    keywords = [
        'WHISKY', 'BRANDY', 'VODKA', 'WINE',  # Liquor
        'CIGARETTE', 'TOBACCO',               # Tobacco
        'ABALONE', 'SCALLOP',                 # High Value Canned
        'MILK POWDER', 'PEDIASURE', 'ENSURE'  # Milk Powder
    ]
    
    if any(k in desc for k in keywords):
        return "🔒 Controlled Item (Double Count)"
    return None

def check_wrong_sign_suspicion(row):
    """
    Optional: If Unit Cost is high but variance is exactly -1 or +1.
    This often indicates a specific singular event (one bottle stolen, one box lost).
    """
    if row['qty_diff'] != 0:
        unit_cost = abs(row['val_diff'] / row['qty_diff'])
        # If item costs more than $100 and we lost/gained exactly 1
        if unit_cost > 100 and abs(row['qty_diff']) == 1:
            if row['qty_diff'] == -1:
                return "💎 Single High Value Item MISSING"
            else:
                return "💎 Single High Value Item FOUND"
    return None

# ==========================================
# ⚙️ RULE REGISTRY (The "Open" Part)
# ==========================================
# To add a new rule, just add the function name to this list.
ACTIVE_RULES = [
    check_contra_items,
    check_high_value_loss,
    check_high_value_gain,
    check_controlled_items,
    check_high_qty_loss,
    check_high_qty_gain,
    check_wrong_sign_suspicion
]

def generate_auto_remark(row):
    """
    The Master Engine. It runs the row through every function in ACTIVE_RULES.
    """
    findings = []
    
    for rule in ACTIVE_RULES:
        try:
            result = rule(row)
            if result:
                findings.append(result)
        except Exception:
            continue
            
    return " | ".join(findings)