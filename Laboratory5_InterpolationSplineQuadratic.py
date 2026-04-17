import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Quadratic Spline Interpolation              #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given Data
x = np.array([8, 11, 15, 18], dtype=float)
y = np.array([5, 9, 10, 8], dtype=float)
n_intervals = len(x) - 1  # Number of splines (N)

# The total number of unknowns is 3 * n_intervals (a, b, c for each interval)
num_unknowns = 3 * n_intervals

# Initialize Matrix Z (A in Ax=V) and Vector V (Results)
Z = np.zeros((num_unknowns, num_unknowns))
V = np.zeros(num_unknowns)

# 1. Filling Matrix from point matching (2*N equations)
# Each spline segment i must pass through (x_i, y_i) and (x_{i+1}, y_{i+1})
j = 0 # index for x and y
f = 0 # index for coefficient columns
for i in range(1, 2 * n_intervals, 2):
    # Equation for the left point of the interval
    Z[i, f:f+3] = [x[j]**2, x[j], 1]
    V[i] = y[j]
    
    j += 1
    
    # Equation for the right point of the interval
    Z[i+1, f:f+3] = [x[j]**2, x[j], 1]
    V[i+1] = y[j]
    
    f += 3

# 2. Filling Matrix from smoothing condition (N-1 equations)
# The derivative (2ax + b) must be equal at the internal knots
j = 0 # index for coefficient columns
l = 1 # index for internal x points
for i in range(2 * n_intervals + 1, num_unknowns):
    # 2*a_i*x + b_i - 2*a_{i+1}*x - b_{i+1} = 0
    Z[i, j:j+2] = [2 * x[l], 1]
    Z[i, j+3:j+5] = [-2 * x[l], -1]
    j += 3
    l += 1

# 3. Boundary Condition: a1 = 0 (makes the first spline linear)
Z[0, 0] = 1
V[0] = 0

# 4. Solving the system [Z][Coeff] = [V]
Coeff = np.linalg.solve(Z, V)

# Plotting
plt.figure(figsize=(10, 6))

j = 0
for i in range(n_intervals):
    # Generate points for the current spline segment
    x_range = np.linspace(x[i], x[i+1], 100)
    # y = a*x^2 + b*x + c
    y_curve = Coeff[j]*x_range**2 + Coeff[j+1]*x_range + Coeff[j+2]
    
    plt.plot(x_range, y_curve, linewidth=2, label=f'Spline {i+1}')
    j += 3

# Add original data points
plt.scatter(x, y, color='red', s=50, zorder=5, label='Data Points')

# Formatting
plt.xlim([min(x)-2, max(x)+2])
plt.ylim([min(y)-2, max(y)+2])
plt.xlabel('x')
plt.ylabel('y')
plt.title('Quadratic Spline Interpolation')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.show()
