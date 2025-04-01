"""
This app uses Python and libraries to generate random numbers, create data frames, plot data points.
"""

import pandas as pd                     # Data manipulation and analysis library
import random                           # Library for generating random numbers    
import numpy as np                      # Library for numerical operations
import matplotlib.pyplot as plt         # Library for data visualization


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
Security:
- Ensure no vulnerabilties are exploited in the code.
- Use secure random number generation methods.
Error Handling:
- Raise a ValueError if x_range is not a tuple of two integers.
- Raise a ValueError if x_range[0] is greater than x_range[1].
Examples:
- gendata((0, 100)) generates a data frame with 'x' values between 0 and 100.
- gendata((-100, 100)) generates a data frame with 'x' values between -100 and 100.
"""
def gendatapoints(x_range):
    # Validate input
    if not isinstance(x_range, tuple) or len(x_range) != 2 or not all(isinstance(i, int) for i in x_range):
        raise ValueError("x_range must be a tuple of two integers.")
    if x_range[0] >= x_range[1]:
        raise ValueError("x_range[0] must be less than x_range[1].")
    
    # Generate random x values
    x_values = [random.randint(x_range[0], x_range[1]) for _ in range(100)]
    
    # Generate y values with noise
    y_values = [x ** 1.5 + random.uniform(-10, 10) for x in x_values]
    
    # Create a DataFrame
    df = pd.DataFrame({'x': x_values, 'y': y_values})
    
    # Sort the DataFrame by 'x'
    df.sort_values(by='x', inplace=True)
    
    return df

"""
Create a function 'plotdata' that takes a pandas data frame and plots the data points.
Arguments:
- 'df' is a pandas data frame with two columns, 'x' and 'y'.
Returns:
- None
Details:
- The function uses matplotlib to create a scatter plot of the data points.
- The x-axis is labeled 'x' and the y-axis is labeled 'y'.
- The plot is displayed using plt.show().
- The plot has a title 'Scatter Plot of Data Points'.
- The points are colored blue and have a size of 10.
- The points are not connected by lines
"""

def plotdata(df):
    """
    Plots a scatter plot of data points from a given DataFrame.
    Parameters:
    df (pandas.DataFrame): A DataFrame containing the data to be plotted. 
                           It must include columns 'x' and 'y'.
    Raises:
    ValueError: If the DataFrame does not contain 'x' and 'y' columns.
    The function creates a scatter plot with 'x' values on the x-axis and 
    'y' values on the y-axis. The plot includes axis labels and a title.
    Assumes the input DataFrame 'df' is sorted by the 'x' column for correct visualization.
    """
    # Define a constant for figure size
    FIGURE_SIZE = (10, 6)
    
    # Validate DataFrame columns
    if not {'x', 'y'}.issubset(df.columns):
        raise ValueError("The DataFrame must contain 'x' and 'y' columns.")
    
    # Create a scatter plot
    plt.figure(figsize=FIGURE_SIZE)
    plt.scatter(df['x'], df['y'], color='blue', s=10)
    
    # Set labels and title
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Scatter Plot of Data Points')
    
    # Show the plot
    plt.show() 
