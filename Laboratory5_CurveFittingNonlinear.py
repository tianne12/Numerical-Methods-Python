import numpy as np
import matplotlib.pyplot as plt

################################################
#  Numerical Methods                           #
#  Engr. Mary Christianne Edjan                #
#                                              #
#  Nonlinear Equation (Linearized Form)        #
#  Curve Fitting and Interpolation             #
#  Python Code                                 #
################################################

# Given data
texp = np.arange(2, 31, 2)
vexp = np.array([9.7, 8.1, 6.6, 5.1, 4.4, 3.7, 2.8, 2.4, 2.0, 1.6, 1.4, 1.1, 0.85, 0.69, 0.6])

# Main Code
vexpLOG = np.log(vexp)  # Natural log to linearize: ln(v) = ln(b) + a1*t
R = 5e6

x = texp
y = vexpLOG
nx = len(x)
ny = len(y)

if nx != ny:
    print('ERROR: The number of elements in x must be the same as in y.')
    a1 = a0 = None
else:
    # Linear Least Squares on the LOG data
    Sx = np.sum(x)
    Sy = np.sum(y)
    Sxy = np.sum(x * y)
    Sxx = np.sum(x**2)
    
    denominator = (nx * Sxx - Sx**2)
    a1 = (nx * Sxy - Sx * Sy) / denominator
    a0 = (Sxx * Sy - Sxy * Sx) / denominator

    # Transform back to nonlinear parameters
    # If ln(v) = a0 + a1*t, then v = exp(a0) * exp(a1*t)
    b = math.exp(a0) if 'math' in globals() else np.exp(a0)
    C = -1 / (R * a1)

    print(f"Coefficient b (V0): {b:.6f}")
    print(f"Capacitance C: {C:.6e} F")
    print(f"Slope a1: {a1:.6f}")

# Plotting
if a1 is not None:
    # Generate smooth curve for the fit
    t = np.arange(0, 30.5, 0.5)
    v = b * np.exp(a1 * t)
    
    plt.figure(figsize=(10, 6))
    
    # Plot experimental data
    plt.plot(texp, vexp, 'ro', markersize=10, label='Experimental Data (vexp)')
    
    # Plot the nonlinear fit
    plt.plot(t, v, 'k', linewidth=2, label=f'Fit: v = {b:.2f} * exp({a1:.4f}t)')
    
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('VT (V)', fontsize=14)
    plt.title('Nonlinear Curve Fitting (Exponential Decay)', fontsize=16)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    plt.show()
