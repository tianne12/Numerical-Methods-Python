import numpy as np

########################################
#  Numerical Methods                   #
#  Numerical Differentiation           #
#  Python Code                         #
########################################

# Setting high precision display
np.set_printoptions(precision=15)

# Task 1: Differentiation from discrete data points
x1 = np.arange(0.398, 0.4021, 0.001)
y1 = np.array([0.408591, 0.409671, 0.410752, 0.411834, 0.4129115])
h1 = 0.001

# f1_a: 3-point Forward/Backward Difference formula
# Note: Python is 0-indexed. y1(2) in Octave is y1[1] in Python.
f1_a = ((-3 * y1[1]) + (4 * y1[2]) - (y1[3])) / (2 * h1)

# f1_b: 3-point Central Difference formula
f1_b = (y1[2] - y1[0]) / (2 * h1)


# Task 2: Differentiation from a functional relationship
def F(x):
    return (2 * x - 1) / (((x**4) * np.sin(x)) + x + 1)**(1/4)

x2 = np.arange(1.96, 2.041, 0.02)
h2 = 0.02

# Evaluate function at specific points
F1 = F(x2[0])
F2 = F(x2[1])
F3 = F(x2[2])
F4 = F(x2[3])
F5 = F(x2[4])

# f2_1: 5-point formula for the First Derivative
f2_1 = (F1 - (8 * F2) + (8 * F4) - F5) / (12 * h2)

# f2_2: 5-point formula for the Second Derivative
f2_2 = ((-F1) + (16 * F2) - (30 * F3) + (16 * F4) - (F5)) / (12 * (h2**2))

# Results Output
print(f"Results for Set 1:")
print(f"f1_a: {f1_a:.12f}")
print(f"f1_b: {f1_b:.12f}")
print("-" * 20)
print(f"Results for Set 2:")
print(f"f2_1 (First Derivative):  {f2_1:.12f}")
print(f"f2_2 (Second Derivative): {f2_2:.12f}")
