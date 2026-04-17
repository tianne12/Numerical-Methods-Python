import math

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Open Method                         #
#  Fixed Point Iteration Method        #
#  Python Code                         #
########################################

# Initial condition
Xest = 1.0

# Setting of parameters
Err_limit = 0.0001
imax = 60

# Display header
print(f"{'i':>3}     {'Xi':>9}     {'Xi+1':>9}     {'Error':>9}")

# Main code
found = False
for i in range(1, imax + 1):
    
    # f(x) rearranged as g(x) for fixed point: Xi+1 = sqrt(cos(Xest)/0.8)
    # Ensure the value inside sqrt is positive to avoid math errors
    Xi = math.sqrt(math.cos(Xest) / 0.8)
    
    # Calculation of error
    Error = abs((Xi - Xest) / Xest)
    
    # Display answer with formatting
    print(f"{i:3d}   {Xest:.6f}   {Xi:.6f}   {Error:.6f}")
    
    # Check convergence (when to stop the iteration)
    if Error < Err_limit:
        Xs = Xi
        print(f"\nConverged Solution: {Xs:.10f}")
        found = True
        break
    
    # Update Xest for the next iteration
    Xest = Xi

# Iteration limit check
if not found:
    print(f"\nSolution was not obtained in {imax} iterations.")
    Xs = "No answer"
