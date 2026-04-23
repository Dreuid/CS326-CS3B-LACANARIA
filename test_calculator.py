# test_calculator.py
import pytest
from calculator import calculate_gwa

# Test 1: Standard GWA calculation
def test_calculate_gwa_normal():
    courses = [{'grade': 1.5, 'units': 3}, {'grade': 2.0, 'units': 3}]
    assert calculate_gwa(courses) == 1.75

# Test 2: Perfect grades
def test_calculate_gwa_perfect():
    courses = [{'grade': 1.0, 'units': 3}, {'grade': 1.0, 'units': 4}]
    assert calculate_gwa(courses) == 1.00

# Test 3: Empty list (no courses added yet)
def test_calculate_gwa_empty():
    assert calculate_gwa([]) == 0.0

# Test 4: Edge case of 0 total units (ZeroDivisionError check)
def test_calculate_gwa_zero_units():
    courses = [{'grade': 1.5, 'units': 0}]
    assert calculate_gwa(courses) == 0.0

# Test 5: Rounding to 2 decimal places
def test_calculate_gwa_rounding():
    # Math: (1.25*3 + 1.75*4) / 7 = 10.75 / 7 = 1.5357... rounds to 1.54
    courses = [{'grade': 1.25, 'units': 3}, {'grade': 1.75, 'units': 4}]
    assert calculate_gwa(courses) == 1.54
