"""
This app uses Python, and uses libraries to generate random numbers, create data frames, and plot graphs.
"""

import random                           # Importing the random library to generate random numbers
import pandas as pd                     # Importing the pandas library to create data frames  
import matplotlib.pyplot as plt         # Importing the matplotlib library to plot graphs
import numpy as np                      # Importing the numpy library to create arrays and perform mathematical operations

"""
Create a function 'gendatapoints' that generates a set of 100 data points (x, f(x)) and returns them as a pandas data frame.
Arguments:
- 'x_range' is a tuple of two integers representing the rang0 e of x values to generate.
Returns:
- A pandas data frame with two columns, 'x' and 'y'.
Details:
- 'x' values are generated randomly between x_range[0] and x_range[1].
- 'y' values are generated as a non-linear function of x with excessive random noise: y = x ^ 1.5  + noise.
- The data frame is sorted by the 'x' values.
- The data frame has 100 rows.
Error Handling:
- Raise a ValueError if x_range is not a tuple of two integers.
- Raise a ValueError if x_range[0] is greater than x_range[1].
Examples:
- gendata((0, 100)) generates a data frame with 'x' values between 0 and 100.
- gendata((-100, 100)) generates a data frame with 'x' values between -100 and 100.
"""

def gen_data_points(x_range):
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


"""
Create a function 'plotdata' that takes a pandas data frame and plots the data points (x, f(x)) using matplotlib.
Arguments:
- 'df' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- The function should create a scatter plot of 'x' vs 'y'.
- The plot should have appropriate labels for the axes and a title.
- The function should display the plot using plt.show().
Error Handling:
- Raise a ValueError if df is not a pandas data frame.
"""

def plot_data(df):
    # Check if df is a pandas data frame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas data frame.")
    
    # Create a scatter plot of 'x' vs 'y'
    plt.scatter(df['x'], df['y'], color='blue', label='Data Points')
    
    # Set the title and labels for the axes
    plt.title('Scatter Plot of Data Points')
    plt.xlabel('x')
    plt.ylabel('y')
    
    # Display the plot
    plt.legend()
    plt.show()