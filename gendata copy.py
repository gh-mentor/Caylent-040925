"""
This app uses Python, and uses libraries to generate random numbers, create data frames, and plot graphs.
"""

import random                           # Importing the random library to generate random numbers
import pandas as pd                     # Importing the pandas library to create data frames  
import matplotlib.pyplot as plt         # Importing the matplotlib library to plot graphs
import numpy as np                      # Importing the numpy library to create arrays and perform mathematical operations


def gen_data_points(x_range):
    """
    Generate a pandas DataFrame containing random data points.
    This function generates a DataFrame with two columns, 'x' and 'y'. The 'x' values
    are random integers within the specified range, and the 'y' values are calculated
    as a non-linear function of 'x' with added random noise.
    Parameters:
        x_range (tuple): A tuple of two integers specifying the range of 'x' values.
                         The first value must be less than the second value.
    Returns:
        pandas.DataFrame: A DataFrame with two columns:
                          - 'x': Random integers within the specified range.
                          - 'y': Non-linear function of 'x' with random noise.
    Raises:
        ValueError: If `x_range` is not a tuple of two integers.
        ValueError: If the first value in `x_range` is not less than the second value.
    """
    # Check if x_range is a tuple of two integers
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(i, int) for i in x_range):
        raise ValueError("x_range must be a tuple of two integers.")
    
    # Check if x_range[0] is less than x_range[1]
    if x_range[0] > x_range[1]:
        raise ValueError("x_range[0] must be less than x_range[1].")
    
    # Generate random 'x' values between x_range[0] and x_range[1]
    x = [random.randint(x_range[0], x_range[1]) for _ in range(100)]
    
    # Generate 'y' values as a non-linear function of 'x' with excessive random noise
    y = [i ** 1.5 + random.uniform(-50, 50) for i in x]
    
    # Create a pandas data frame with 'x' and 'y' columns
    df = pd.DataFrame({'x': x, 'y': y})
    
    # Sort the data frame by 'x' values
    df.sort_values(by='x', inplace=True)
    
    return df



def plot_data(df, title='Scatter Plot of Data Points', color='blue'):
    """
    Plots a scatter plot of data points from a pandas DataFrame.
    Parameters:
    -----------
    df : pandas.DataFrame
        A DataFrame containing the data to be plotted. It must have columns 'x' and 'y'.
    title : str, optional
        The title of the scatter plot. Default is 'Scatter Plot of Data Points'.
    color : str, optional
        The color of the data points in the scatter plot. Default is 'blue'.
    Raises:
    -------
    ValueError
        If the input `df` is not a pandas DataFrame.
    Notes:
    ------
    This function assumes that the DataFrame `df` contains numeric columns named 'x' and 'y'.
    Example:
    --------
    >>> import pandas as pd
    >>> import matplotlib.pyplot as plt
    >>> data = {'x': [1, 2, 3], 'y': [4, 5, 6]}
    >>> df = pd.DataFrame(data)
    >>> plot_data(df, title='Example Plot', color='red')
    """
    # Check if df is a pandas data frame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas data frame.")
    
    # Create a scatter plot of 'x' vs 'y'
    plt.scatter(df['x'], df['y'], color=color, label='Data Points')
    
    # Set the title and labels for the axes
    plt.title(title)
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Display the plot
    plt.legend()
    plt.show()