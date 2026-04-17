import math

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne Edjan        #
#                                      #
#  Bracketing Method                   #
#  False Position Method               #
#  Python Code                         #
########################################

# Define the function f(x)
def F(x):
    return x - 2 * (math.exp(-x))

# Initial condition
a = 0.0
b = 1.0

# Setting of parameters
imax = 30
err_limit = 0.001
Fa = F(a)
Fb = F(b)

# Main Code
if Fa * Fb > 0:
    # Stop the program if the function has the same sign at points a and b
    print("Error: The function has the same sign at points a and b.")
else:
    # Display Header
    print(f"{'iteration':<10} {'a':<12} {'b':<12} {'(xNS)':<12} {'f(xNS)':<15} {'Error':<12}")
    print("-" * 80)

    for i in range(1, imax + 1):
        # Update Fa and Fb for the current a and b
        Fa = F(a)
        Fb = F(b)
        
        # Calculate the numerical solution (False Position Formula)
        xNS = ((a * Fb) - (b * Fa)) / (Fb - Fa)
        
        # Calculate the current estimated error
        # Note: Avoid division by zero if b is 0
        erro = abs((b - a) / b) if b != 0 else 0
        
        FxNS = F(xNS)
        
        # Display Iteration results
        print(f"{i:3d}        {a:11.6f}    {b:11.6f}    {xNS:11.6f}    {FxNS:11.6f}    {erro:11.6f}")

        # Stop if an exact solution is found
        if FxNS == 0:
            print(f"\nAn exact solution x ={xNS:11.6f} was found")
            break

        # Stop if the error is smaller than the desired limit
        if erro < err_limit:
            print(f"\nConverged Solution xNS: {xNS:11.6f}")
            break

        # Stop if max iterations reached
        if i == imax:
            print(f"\nSolution was not obtained in {imax} iterations")
            break

        # Determine the next interval
        if F(a) * FxNS < 0:
            b = xNS
        else:
            a = xNS
