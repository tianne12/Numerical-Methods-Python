import math

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Open Method                         #
#  Secant Method                       #
#  Python Code                         #
########################################

# Define the function f(x)
def F(x):
    return x - (2 * (math.exp(-x)))

# Initial conditions
Xa = 0.0
Xb = 1.0

# Setting of parameters
Err_limit = 0.0001
imax = 10

print(f"{'i':<5} {'Xi':<15} {'Error':<15}")
print("-" * 40)

# Main Code
found = False
for i in range(1, imax + 1):
    
    # Evaluate function at current points
    yXb = F(Xb)
    yXa = F(Xa)
    
    # Equation for Xi (Secant Formula)
    # Using the slope between (Xa, yXa) and (Xb, yXb)
    try:
        Xi = Xb - (yXb * (Xa - Xb)) / (yXa - yXb)
    except ZeroDivisionError:
        print("Error: Division by zero in Secant formula.")
        break

    # Calculation of error
    current_error = abs((Xi - Xb) / Xb) if Xb != 0 else 0
    
    # Print progress
    print(f"{i:<5} {Xi:<15.10f} {current_error:<15.10f}")

    # Check for convergence
    if current_error < Err_limit:
        Xs = Xi
        print(f"\nFinal Solution (Xs): {Xs:.10f}")
        found = True
        break
    
    # Update points for next iteration
    Xa = Xb
    Xb = Xi

# Iteration limit check
if not found:
    print(f"\nSolution was not obtained in {imax} iterations.")
    Xs = "No answer"
