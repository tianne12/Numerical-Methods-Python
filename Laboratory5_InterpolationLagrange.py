import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Linear Interpolation (Lagrange)             #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given data
x = np.array([1, 2, 4, 5, 7])
y = np.array([52, 5, -5, -40, 10])
Xint = 3

# Main Code
n = len(x)
L = np.ones(n)  # Initialize L with 1s

for i in range(n):
    for j in range(n):
        if j != i:
            # Lagrange basis polynomial calculation
            L[i] = L[i] * (Xint - x[j]) / (x[i] - x[j])

# The interpolated value is the sum of y_i * L_i
Yint = np.sum(y * L)

print(f"Interpolated value at x = {Xint}: {Yint:.4f}")

# Plotting
plt.figure(figsize=(10, 6))

# Plot the original data points
plt.plot(x, y, 'ro', markersize=9, label='Data Points')

# Plot the lines connecting the data points (Linear style)
plt.plot(x, y, 'k', linewidth=2, label='Linear Connection')

# Plot the specific interpolated point
plt.plot(Xint, Yint, 'gs', markersize=10, label=f'Interpolated Point (x={Xint})')

plt.xlabel('x', fontsize=14)
plt.ylabel('y', fontsize=14)
plt.title('Lagrange Interpolation', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
