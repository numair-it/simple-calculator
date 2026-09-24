"""
Automated Verification Suite for Simple Calculator
Course: Learning Manual Testing (OUSL)
Validates all manual test cases against Calculator v2.0.0
"""

import unittest
from calculator import add, subtract, multiply, divide, modulus, power, square_root

class TestCalculatorV2(unittest.TestCase):
    
    # TC_CALC_001
    def test_tc001_addition_positive(self):
        self.assertEqual(add(15, 25), 40.0)

    # TC_CALC_002
    def test_tc002_addition_negative(self):
        self.assertEqual(add(-10, 30), 20.0)

    # TC_CALC_003
    def test_tc003_addition_decimal(self):
        self.assertAlmostEqual(add(12.35, 7.65), 20.0, places=2)

    # TC_CALC_004
    def test_tc004_subtraction_positive(self):
        self.assertEqual(subtract(50, 20), 30.0)

    # TC_CALC_005
    def test_tc005_subtraction_negative_result(self):
        self.assertEqual(subtract(10, 45), -35.0)

    # TC_CALC_006
    def test_tc006_subtraction_decimal(self):
        self.assertAlmostEqual(subtract(25.75, 10.25), 15.5, places=2)

    # TC_CALC_007
    def test_tc007_multiplication_positive(self):
        self.assertEqual(multiply(12, 8), 96.0)

    # TC_CALC_008
    def test_tc008_multiplication_zero(self):
        self.assertEqual(multiply(45, 0), 0.0)

    # TC_CALC_009
    def test_tc009_multiplication_negatives(self):
        self.assertEqual(multiply(-6, -7), 42.0)

    # TC_CALC_010
    def test_tc010_division_positive(self):
        self.assertEqual(divide(100, 4), 25.0)

    # TC_CALC_011
    def test_tc011_division_recurring(self):
        self.assertAlmostEqual(divide(10, 3), 3.3333333333333335, places=5)

    # TC_CALC_012 (BUG-001 Fixed)
    def test_tc012_division_by_zero(self):
        result = divide(50, 0)
        self.assertEqual(result, "Error: Division by zero is not allowed.")

    # TC_CALC_013
    def test_tc013_modulus_positive(self):
        self.assertEqual(modulus(29, 5), 4.0)

    # TC_CALC_014 (BUG-002 Fixed)
    def test_tc014_modulus_by_zero(self):
        result = modulus(20, 0)
        self.assertEqual(result, "Error: Modulo by zero is not allowed.")

    # TC_CALC_015
    def test_tc015_power_positive(self):
        self.assertEqual(power(2, 8), 256.0)

    # TC_CALC_016
    def test_tc016_power_zero_exponent(self):
        self.assertEqual(power(99, 0), 1.0)

    # TC_CALC_017
    def test_tc017_square_root_positive(self):
        self.assertEqual(square_root(64), 8.0)

    # TC_CALC_018 (BUG-003 Fixed)
    def test_tc018_square_root_negative(self):
        result = square_root(-25)
        self.assertEqual(result, "Error: Cannot calculate square root of a negative number.")

if __name__ == "__main__":
    print("\nRunning Calculator v2.0.0 Verification Suite...")
    unittest.main(verbosity=2)
