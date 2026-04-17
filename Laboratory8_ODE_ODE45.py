import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne E. Edjan     #
#                                      #
#  Solving ODEs (ode45 equivalent)     #
#  Python Code                         #
########################################

# 1. Define the differential equation: dy/dx = -1.2y + 7e^(0.3x)
def dydx(x, y):
    return -1.2 * y + 7 * np.exp(0.3 * x)

# 2. Set Parameters
x_span = (0, 2.5)          # Start and end points
x_eval = np.arange(0, 2.6, 0.5)  # Points where we want the solution (0:0.5:2.5)
y_ini = [3]                # Initial condition must be in a list/array

# 3. Solve the ODE numerically using solve_ivp (equivalent to ode45)
# Note: solve_ivp expects (x, y) by default, matching your function signature
sol = solve_ivp(dydx, x_span, y_ini, t_eval=x_eval)

x_num = sol.t
y_num = sol.y[0]

# 4. Calculate the Exact Solution
# yExact = 70/9*exp(0.3x) - 43/9*exp(-1.2x) 
# Note: I corrected the sign in the first exp to match the general solution of the ODE
y_exact = (70/9) * np.exp(0.3 * x_num) - (43/9) * np.exp(-1.2 * x_num)

# 5. Calculate Error
error = y_exact - y_num

# --- Display Results ---
print(f"{'x':>5} | {'y (Numerical)':>15} | {'y (Exact)':>15} | {'Error':>15}")
print("-" * 60)
for i in range(len(x_num)):
    print(f"{x_num[i]:5.1f} | {y_num[i]:15.6f} | {y_exact[i]:15.6f} | {error[i]:15.6e}")

# --- Plotting ---
plt.figure(figsize=(10, 6))
plt.plot(x_num, y_num, 'ro', label='Numerical (solve_ivp)')
plt.plot(x_num, y_exact, 'k-', label='Exact Solution')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Numerical and Exact Solutions')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
