import math

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Open Method                         #
#  Newton-Raphson Method               #
#  Python Code                         #
########################################

# Define the function f(x)
def F(x):
    return x - (2 * math.exp(-x))

# Define the first derivative f'(x)
# f'(x) = 1 + 2*exp(-x)
def dF(x):
    return 1 + (2 * math.exp(-x))

# Initial condition
Xest = 1.0

# Setting of parameters
Err_limit = 0.0001
imax = 10

print(f"{'i':<5} {'Xi':<12} {'Error':<12}")
print("-" * 30)

# Main Code
found = False
for i in range(1, imax + 1):
    y1 = F(Xest)
    y2 = dF(Xest)
    
    # Equation for xNS (Newton-Raphson Formula)
    Xi = Xest - y1 / y2
    
    # Calculation of error
    current_error = abs((Xi - Xest) / Xest)
    
    # Display iteration details
    print(f"{i:<5} {Xi:<12.8f} {current_error:<12.8f}")
    
    # Check convergence
    if current_error < Err_limit:
        Xs = Xi
        print(f"\nFinal Solution (Xs): {Xs:.10f}")
        found = True
        break
    
    # Update Xest for the next iteration
    Xest = Xi

# Iteration limit check
if not found:
    print(f"\nSolution was not obtained in {imax} iterations.")
    Xs = "No answer"
