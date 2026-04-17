import numpy as np
import matplotlib.pyplot as plt

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Numerical Differentiation           #
#  Python Code                         #
########################################

# Given
t = np.arange(4, 8.1, 0.2)  # 4 to 8 with step 0.2
x = np.array([-5.87, -4.23, -2.55, -0.89, 0.67, 2.09, 3.31, 4.31, 5.06, 5.55, 
              5.78, 5.77, 5.52, 5.08, 4.46, 3.72, 2.88, 2.00, 1.10, 0.23, -0.59])

# Main Code
n = len(t)

# --- Velocity Calculation ---
vel = np.zeros(n)
# Forward difference for the first point
vel[0] = (x[1] - x[0]) / (t[1] - t[0])
# Central difference for interior points
for i in range(1, n - 1):
    vel[i] = (x[i+1] - x[i-1]) / (t[i+1] - t[i-1])
# Backward difference for the last point
vel[n-1] = (x[n-1] - x[n-2]) / (t[n-1] - t[n-2])

# --- Acceleration Calculation ---
acc = np.zeros(n)
# Forward difference for the first point
acc[0] = (vel[1] - vel[0]) / (t[1] - t[0])
# Central difference for interior points
for i in range(1, n - 1):
    acc[i] = (vel[i+1] - vel[i-1]) / (t[i+1] - t[i-1])
# Backward difference for the last point
acc[n-1] = (vel[n-1] - vel[n-2]) / (t[n-1] - t[n-2])

# --- Plotting ---
plt.figure(figsize=(8, 10))

# Distance Plot
plt.subplot(3, 1, 1)
plt.plot(t, x, 'b.-')
plt.ylabel('Distance')
plt.title('Numerical Differentiation')

# Velocity Plot
plt.subplot(3, 1, 2)
plt.plot(t, vel, 'r.-')
plt.ylabel('Velocity')

# Acceleration Plot
plt.subplot(3, 1, 3)
plt.plot(t, acc, 'g.-')
plt.ylabel('Acceleration')
plt.xlabel('Time')

plt.tight_layout()
plt.show()
