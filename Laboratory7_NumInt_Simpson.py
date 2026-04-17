import numpy as np

########################################
#  Numerical Methods                   #
#  Engr. Mary Christianne E. Edjan     #
#                                      #
#  Simpson's 1/3 and 3/8 Rules         #
#  Python Code                         #
########################################

# Define the function f(x)
def f(x):
    return (np.sin(x))**2

# User Inputs
try:
    a = float(input('Enter lower limit a: '))
    b = float(input('Enter upper limit b: '))
    N = int(input('Enter number of subintervals: '))
    method_choice = input('Which Simpson Method are you going to use (1/3 or 3/8)? ')
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()

h = (b - a) / N

# --- Simpson's 1/3 Rule ---
if method_choice == '1/3':
    # N must be even for Simpson's 1/3 Rule
    if N % 2 != 0:
        print('Warning: Simpson 1/3 requires an even number of subintervals.')
        N = int(input('Enter even number of subintervals: '))
        h = (b - a) / N

    # Generate internal points
    k = np.arange(1, N)
    S = f(a + k * h)
    
    # Python is 0-indexed: 
    # S[0] is index 1 (odd), S[1] is index 2 (even), etc.
    # Note: Logic follows the pattern: f(a) + 4(odd) + 2(even) + f(b)
    # Based on index starting at 1:
    S_odd = np.sum(S[0::2])  # Indices 1, 3, 5...
    S_even = np.sum(S[1::2]) # Indices 2, 4, 6...

    out = (h / 3) * (f(a) + 4 * S_odd + 2 * S_even + f(b))
    print(f'The value of integration is {out:.6f}')

# --- Simpson's 3/8 Rule ---
elif method_choice == '3/8':
    # N must be a multiple of 3 for Simpson's 3/8 Rule
    if N % 3 != 0:
        print('Warning: Simpson 3/8 requires subintervals divisible by 3.')
        N = int(input('Enter a divisible of 3 number of subintervals: '))
        h = (b - a) / N

    k = np.arange(1, N)
    S = f(a + k * h)
    
    # S3 contains indices that are multiples of 3 (the "2" coefficients)
    # S_others contains the rest (the "3" coefficients)
    s3_indices = np.arange(2, len(S), 3)
    S3 = np.sum(S[s3_indices])
    
    # Create a mask to sum everything except the multiples of 3
    mask = np.ones(len(S), dtype=bool)
    mask[s3_indices] = False
    S_others = np.sum(S[mask])

    out = (3 * h / 8) * (f(a) + 3 * S_others + 2 * S3 + f(b))
    print(f'The value of integration is {out:.6f}')

else:
    print('Method choice not recognized. Please use "1/3" or "3/8".')
