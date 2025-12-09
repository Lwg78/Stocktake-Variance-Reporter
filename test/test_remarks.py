import sys
import os
import pytest
import pandas as pd

# Add the project root to the Python path to allow imports from `src`
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Import the specific logic we want to test
from src.remarks_engine import generate_auto_remark

# --- TEST CASE 1: The "Contra" Item ---
def test_contra_detection():
    # 1. ARRANGE: Create a fake row of data
    fake_row = pd.Series({
        'description': 'DA - SADIA CHICKEN WINGS',
        'val_diff': -100,
        'qty_diff': -10
    })
    
    # 2. ACT: Run your engine
    result = generate_auto_remark(fake_row)
    
    # 3. ASSERT: Check if the AI guessed right
    # We expect the specific alert string we wrote in the engine
    assert "Contra/Pkg Change?" in result

# --- TEST CASE 2: The "Theft" (High Value Loss) ---
def test_high_value_loss():
    fake_row = pd.Series({
        'description': 'NORMAL SHAMPOO',
        'val_diff': -600,  # Huge loss
        'qty_diff': -50
    })
    
    result = generate_auto_remark(fake_row)
    
    # Verify it flagged as LOSS, not Gain
    assert "High Value LOSS" in result
    assert "Investigate Theft" in result

# --- TEST CASE 3: The "Normal" Item (No Remarks) ---
def test_normal_item():
    fake_row = pd.Series({
        'description': 'APPLES',
        'val_diff': 5,     # Tiny variance
        'qty_diff': 1
    })
    
    result = generate_auto_remark(fake_row)
    
    # Expect empty string (no alarms)
    assert result == ""