import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Linear Least Squares Regression             #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given data
# np.arange(start, stop, step) - note that 'stop' is exclusive
x = np.arange(0, 101, 10) 
y = np.array([0.94, 0.96, 1.0, 1.05, 1.07, 1.09, 1.14, 1.17, 1.21, 1.24, 1.28])

# Main Code
nx = len(x)
ny = len(y)

if nx != ny:
    print('ERROR: The number of elements in x must be the same as in y.')
    a1 = None
    a0 = None
else:
    # Calculate the summation terms using NumPy's efficient methods
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxy = np.sum(x * y)
    Sxx = np.sum(x**2)
    
    # Calculate the coefficients a1 (slope) and a0 (intercept)
    denominator = (nx * Sxx - Sx**2)
    a1 = (nx * Sxy - Sx * Sy) / denominator
    a0 = (Sxx * Sy - Sxy * Sx) / denominator
    
    print(f"Coefficient a1 (Slope): {a1:.6f}")
    print(f"Coefficient a0 (Intercept): {a0:.6f}")

# Plotting
if a1 is not None:
    # Define plot range
    Tplot = np.array([-300, 100])
    pplot = a1 * Tplot + a0
    
    plt.figure(figsize=(10, 6))
    
    # Plot original data points as red stars
    plt.plot(x, y, '*r', markersize=12, label='Data Points')
    
    # Plot the regression line in black
    plt.plot(Tplot, pplot, 'k', linewidth=2, label='Linear Regression')
    
    # Labels and formatting
    plt.xlabel('Temperature (C)', fontsize=14)
    plt.ylabel('Pressure (atm)', fontsize=14)
    plt.title('Linear Least Squares Regression', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    
    # Showing the plot
    plt.show()

# Calculating the specific value T0 from your snippet
# T0 = -a0 / a1 (Solving for x when y = 0)
if a1:
    T0 = -a0 / a1
    print(f"T0: {T0:.4f}")
