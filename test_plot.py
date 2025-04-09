import pytest
import pandas as pd
from gendata import gen_data_points

# filepath: c:\Users\ascop\Documents\Training\Caylent-040125\test_gendata copy.py

def test_gen_data_points_valid_input():
    # Test with a valid range
    x_range = (10, 20)
    df = gen_data_points(x_range)
    
    # Check if the result is a DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # Check if the DataFrame has the correct columns
    assert list(df.columns) == ['x', 'y']
    
    # Check if the 'x' column values are within the specified range
    assert df['x'].between(x_range[0], x_range[1]).all()
    
    # Check if the DataFrame is sorted by 'x'
    assert df['x'].is_monotonic_increasing

def test_gen_data_points_invalid_xrange_type():
    # Test with invalid x_range type
    with pytest.raises(ValueError, match="x_range must be a tuple of two integers."):
        gen_data_points([10, 20])  # Passing a list instead of a tuple

def test_gen_data_points_invalid_xrange_length():
    # Test with invalid x_range length
    with pytest.raises(ValueError, match="x_range must be a tuple of two integers."):
        gen_data_points((10,))  # Passing a tuple with one element

def test_gen_data_points_invalid_xrange_order():
    # Test with x_range[0] >= x_range[1]
    with pytest.raises(ValueError, match="x_range[0] must be less than x_range[1]."):
        gen_data_points((20, 10))  # First value is greater than the second

def test_gen_data_points_edge_case():
    # Test with minimal range
    x_range = (0, 1)
    df = gen_data_points(x_range)
    
    # Check if the result is a DataFrame
    assert isinstance(df, pd.DataFrame)
    
    # Check if the 'x' column values are within the specified range
    assert df['x'].between(x_range[0], x_range[1]).all()