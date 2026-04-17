import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Newton's Divided Difference Interpolation   #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given
x = np.array([1, 2, 4, 5, 7], dtype=float)
y = np.array([52, 5, -5, -40, 10], dtype=float)
Xint = 3

# Main Code
n = len(x)
# Create a table for divided differences initialized with zeros
# Size (n, n) to accommodate all levels of differences
divDIF = np.zeros((n, n))

# The first column is always the y values
divDIF[:, 0] = y

# Calculate divided differences table
# j represents the column (the order of difference)
# i represents the row
for j in range(1, n):
    for i in range(n - j):
        divDIF[i, j] = (divDIF[i + 1, j - 1] - divDIF[i, j - 1]) / (x[i + j] - x[i])

# The coefficients 'a' are the first row of the divDIF table
a = divDIF[0, :]

# Evaluate the polynomial at Xint
Yint = a[0]
xn = 1.0
for k in range(1, n):
    xn = xn * (Xint - x[k - 1])
    Yint = Yint + a[k] * xn

print(f"Interpolated value at x = {Xint}: {Yint:.4f}")

# Plotting
plt.figure(figsize=(10, 6))

# Original data points
plt.plot(x, y, 'ro', markersize=9, label='Data Points')

# Linear connection (as per your Octave code style)
plt.plot(x, y, 'k', linewidth=2, label='Linear Connection')

# Highlight the interpolated result
plt.plot(Xint, Yint, 'bs', markersize=10, label=f'Result at x={Xint}')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title("Newton's Divided Difference Interpolation", fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
