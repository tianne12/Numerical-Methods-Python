import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Linear Interpolation (Interval Search)      #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given Data
x = np.array([8, 11, 15, 18], dtype=float)
y = np.array([5, 9, 10, 8], dtype=float)
Xint = 12.7

# Main Code
n = len(x)
idx = 1  # Default to the first possible upper bound

# Search for the interval where Xint resides
for i in range(1, n):
    if Xint < x[i]:
        idx = i
        break

# Linear Interpolation Formula:
# Calculates the y-value on a straight line between x[idx-1] and x[idx]
x_curr = x[idx]
x_prev = x[idx-1]
y_curr = y[idx]
y_prev = y[idx-1]

Yint = (Xint - x_curr) * y_prev / (x_prev - x_curr) + (Xint - x_prev) * y_curr / (x_curr - x_prev)

print(f"Interpolated value at x = {Xint}: {Yint:.4f}")

# Plotting
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.plot(x, y, 'ro', markersize=9, label='Data Points')

# Plot the linear connection (piecewise linear interpolation)
plt.plot(x, y, 'k', linewidth=2, label='Linear Interpolation')

# Highlight the specific interpolated result
plt.plot(Xint, Yint, 'bs', markersize=10, label=f'Result at x={Xint}')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Linear Interpolation (Interval-based)', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
