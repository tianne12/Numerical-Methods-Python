import math

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Bracketing Method                   #
#  Bisection Method                    #
#  Python Code                         #
########################################

# f(x)
def F(x):
    return x - 2 * (math.exp(-x))

# Initial condition
a = 0
b = 1

# Setting of parameters
imax = 20
tol = 0.001
Fa = F(a)
Fb = F(b)

# Main Code
if Fa * Fb > 0:
    # Stop the program if the function has the same sign at points a and b
    print("Error: The function has the same sign at points a and b.")
else:
    # Display Header
    print(f"{'iteration':<10} {'a':<12} {'b':<12} {'(xNS)':<12} {'f(xNS)':<15} {'Tolerance':<12}")
    
    for i in range(1, imax + 1):
        xNS = (a + b) / 2              # Calculate the numerical solution, xNS
        toli = (b - a) / 2             # Calculate the current tolerance
        FxNS = F(xNS)                  # Calculate the value of f(xNS)
        
        # Display Iteration results
        print(f"{i:3d}        {a:11.6f}    {b:11.6f}    {xNS:11.6f}    {FxNS:11.6f}    {toli:11.6f}")

        # Stop if an exact solution is found
        if FxNS == 0:
            print(f"An exact solution x ={xNS:11.6f} was found")
            break

        # Stop if current tolerance is smaller than desired tolerance
        if toli < tol:
            print(f"\nFinal Solution xNS: {xNS:11.6f}")
            break

        # Stop if max iterations reached
        if i == imax:
            print(f"Solution was not obtained in {imax} iterations")
            break

        # Bisection logic: select interval for the next iteration
        if F(a) * FxNS < 0:
            b = xNS
        else:
            a = xNS
