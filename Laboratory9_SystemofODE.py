import numpy as np
import matplotlib.pyplot as plt

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne E. Edjan     #
#                                      #
#  System of ODEs (RK4 Method)         #
#  Python Code                         #
########################################

# 1. Get User Inputs
# Example input for ODE1: lambda t, x, y: y
# Example input for ODE2: lambda t, x, y: -9.81 * np.sin(x)
ode1_str = input('Input 1st ODE (e.g., lambda t, x, y: y): ')
ode2_str = input('Input 2nd ODE (e.g., lambda t, x, y: -9.81 * np.sin(x)): ')

# Convert string inputs to callable functions
ODE1 = eval(ode1_str)
ODE2 = eval(ode2_str)

a = float(input('Input first time value (a): '))
b = float(input('Input last time value (b): '))
h = float(input('Input increment value (h): '))
x1_init = float(input('Input initial value of x: '))
y1_init = float(input('Input initial value of y: '))

# 2. Main Code Setup
n = int((b - a) / h)
t = np.zeros(n + 1)
x = np.zeros(n + 1)
y = np.zeros(n + 1)

# Set initial conditions
t[0] = a
x[0] = x1_init
y[0] = y1_init

# 3. RK4 Iteration for Systems
for i in range(n):
    t_curr = t[i]
    x_curr = x[i]
    y_curr = y[i]
    tm = t_curr + h / 2
    
    # K1 values
    Kx1 = ODE1(t_curr, x_curr, y_curr)
    Ky1 = ODE2(t_curr, x_curr, y_curr)
    
    # K2 values
    Kx2 = ODE1(tm, x_curr + Kx1 * h / 2, y_curr + Ky1 * h / 2)
    Ky2 = ODE2(tm, x_curr + Kx1 * h / 2, y_curr + Ky1 * h / 2)
    
    # K3 values
    Kx3 = ODE1(tm, x_curr + Kx2 * h / 2, y_curr + Ky2 * h / 2)
    Ky3 = ODE2(tm, x_curr + Kx2 * h / 2, y_curr + Ky2 * h / 2)
    
    # K4 values
    t_next = t_curr + h
    Kx4 = ODE1(t_next, x_curr + Kx3 * h, y_curr + Ky3 * h)
    Ky4 = ODE2(t_next, x_curr + Kx3 * h, y_curr + Ky3 * h)
    
    # Update next step
    t[i+1] = t_next
    x[i+1] = x_curr + (Kx1 + 2*Kx2 + 2*Kx3 + Kx4) * h / 6
    y[i+1] = y_curr + (Ky1 + 2*Ky2 + 2*Ky3 + Ky4) * h / 6

# 4. Plot Results
plt.figure(figsize=(10, 6))
plt.plot(t, x, 'b-', linewidth=2, label='x(t) - Angle')
plt.plot(t, y, 'r--', linewidth=1, label='y(t) - Angular Velocity')

plt.xlabel('Time (s)')
plt.ylabel('Values')
plt.title('RK4 Solution for System of ODEs')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
