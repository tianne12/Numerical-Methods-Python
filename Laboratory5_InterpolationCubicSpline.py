import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Cubic Spline Interpolation                  #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

def cubic_splines(x, y, xint):
    n = len(x)
    if n != len(y):
        raise ValueError("ERROR: x and y do not have the same number of points")
    
    # Calculate h_i
    h = np.zeros(n - 1)
    for i in range(n - 1):
        h[i] = x[i+1] - x[i]

    # Initialize vectors for Thomas Algorithm
    # Sizes adjusted for Python's 0-indexing
    b = np.zeros(n - 2)
    a = np.zeros(n - 2)
    d = np.zeros(n - 2)
    r = np.zeros(n - 2)

    # Building the tridiagonal system components
    for i in range(n - 2):
        d[i] = 2 * (h[i] + h[i+1])
        r[i] = 6 * (((y[i+2] - y[i+1]) / h[i+1]) - ((y[i+1] - y[i]) / h[i]))
        
        if i > 0:
            b[i] = h[i]
        if i < n - 3:
            a[i] = h[i+1]

    # Thomas Algorithm (Forward Elimination)
    c_prime = np.zeros(n - 2)
    r_prime = np.zeros(n - 2)

    c_prime[0] = a[0] / d[0]
    r_prime[0] = r[0] / d[0]

    for i in range(1, n - 2):
        denom = d[i] - b[i] * c_prime[i-1]
        if denom == 0:
            raise ZeroDivisionError("Zero in denominator during Thomas Algorithm")
        if i < n - 3:
            c_prime[i] = a[i] / denom
        r_prime[i] = (r[i] - b[i] * r_prime[i-1]) / denom

    # Thomas Algorithm (Back Substitution)
    solution = np.zeros(n - 2)
    solution[n-3] = r_prime[n-3]
    for i in range(n - 4, -1, -1):
        solution[i] = r_prime[i] - c_prime[i] * solution[i+1]

    # Second derivatives (acoeff) - Natural Spline (0 at ends)
    acoeff = np.zeros(n)
    for i in range(1, n - 1):
        acoeff[i] = solution[i-1]

    # Find which interval xint belongs to
    interval = 0
    for j in range(n - 1):
        if x[j] <= xint <= x[j+1]:
            interval = j
            break
    
    i = interval
    # Calculate Interpolation using the Cubic Spline formula
    YintA = (acoeff[i] * ((x[i+1] - xint)**3)) / (6 * h[i])
    YintB = (acoeff[i+1] * ((xint - x[i])**3)) / (6 * h[i])
    YintC = ((y[i] / h[i]) - (acoeff[i] * h[i] / 6)) * (x[i+1] - xint)
    YintD = ((y[i+1] / h[i]) - (acoeff[i+1] * h[i] / 6)) * (xint - x[i])
    
    return YintA + YintB + YintC + YintD

# Given Data
X = np.array([8, 11, 15, 18, 22])
Y = np.array([5, 9, 10, 8, 7])
Xint = np.arange(8, 22.1, 0.1)

# Generate Interpolated Values
y_interpolated = [cubic_splines(X, Y, xi) for xi in Xint]

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(Xint, y_interpolated, 'k', linewidth=2, label='Cubic Spline Curve')
plt.plot(X, Y, 'ro', markersize=9, label='Data Points')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Cubic Spline Interpolation', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
