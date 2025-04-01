import unittest
import pandas as pd
from DataScience.gendata import gendatapoints

# filepath: c:\Users\ascop\Documents\Training\Caylent-040125\DataScience\test_gendata.py

class TestGendatapoints(unittest.TestCase):
    def test_valid_input(self):
        """Test with a valid range."""
        df = gendatapoints((0, 100))
        self.assertEqual(len(df), 100)  # Ensure 100 rows
        self.assertTrue({'x', 'y'}.issubset(df.columns))  # Ensure correct columns
        self.assertTrue(all(df['x'].between(0, 100)))  # Ensure x values are within range

    def test_invalid_input_not_tuple(self):
        """Test with input that is not a tuple."""
        with self.assertRaises(ValueError):
            gendatapoints([0, 100])  # List instead of tuple

    def test_invalid_input_non_integer(self):
        """Test with a tuple containing non-integer values."""
        with self.assertRaises(ValueError):
            gendatapoints((0, "100"))  # String instead of integer

    def test_invalid_input_single_value_tuple(self):
        """Test with a tuple of incorrect length."""
        with self.assertRaises(ValueError):
            gendatapoints((0,))  # Single value tuple

    def test_invalid_input_reversed_range(self):
        """Test with x_range[0] >= x_range[1]."""
        with self.assertRaises(ValueError):
            gendatapoints((100, 0))  # Reversed range

    def test_negative_range(self):
        """Test with a valid negative range."""
        df = gendatapoints((-50, -10))
        self.assertEqual(len(df), 100)  # Ensure 100 rows
        self.assertTrue(all(df['x'].between(-50, -10)))  # Ensure x values are within range

if __name__ == '__main__':
    unittest.main()