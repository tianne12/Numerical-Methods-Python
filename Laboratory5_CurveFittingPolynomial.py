import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Polynomial Regression                       #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given Data
x = np.arange(0, 6.1, 0.4)
y = np.array([0, 3, 4.5, 5.8, 5.9, 5.8, 6.2, 7.4, 9.6, 15.6, 20.7, 26.7, 31.1, 35.6, 39.3, 41.5])

n = len(x)   # Number of data points
m = 4        # Order of the polynomial

# Initialize xsum vector
xsum = np.zeros(2 * m)
for i in range(1, 2 * m + 1):
    xsum[i-1] = np.sum(x**i)

# Initialize matrix [a] and column vector [b]
a = np.zeros((m + 1, m + 1))
b = np.zeros((m + 1, 1))

# Step 3: Fill the matrix [a] and vector [b]
a[0, 0] = n
b[0, 0] = np.sum(y)

# Assign the first row of matrix [a]
for j in range(2, m + 2):
    a[0, j-1] = xsum[j-2]

# Create rows 2 through (m+1) of matrix [a] and vector [b]
for i in range(2, m + 2):
    for j in range(1, m + 2):
        a[i-1, j-1] = xsum[j + i - 3]
    b[i-1, 0] = np.sum((x**(i - 1)) * y)

# Step 4: Solve the system [a][p] = [b]
# np.linalg.solve is the equivalent of the backslash operator (\)
p = np.linalg.solve(a, b).flatten()

# Octave's polyval expects coefficients in descending order (a_n, ..., a_1, a_0)
# Our 'p' is currently ascending (a_0, a_1, ..., a_n), so we flip it
Pcoef = p[::-1]

# Prediction / Fitting
epsilon = np.arange(0, 6.1, 0.1)
stressfit = np.polyval(Pcoef, epsilon)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'ro', markersize=9, label='Original Data')
plt.plot(epsilon, stressfit, 'k', linewidth=2, label=f'{m}th Degree Polynomial Fit')

plt.xlabel('Strain', fontsize=14)
plt.ylabel('Stress (MPa)', fontsize=14)
plt.title('Polynomial Regression', fontsize=16)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Print the coefficients for verification
print("Polynomial Coefficients (descending order):")
print(Pcoef)
