import math

########################################
#  Numerical Methods                   #
#  Gauss-Quadrature Integration        #
#  Python Code                         #
########################################

# Define the function f(x)
def f(x):
    return (math.sin(x))**2

# Get User Input
try:
    a = float(input('Enter lower limit a: '))
    b = float(input('Enter upper limit b: '))
    G = int(input('How many intervals (2-6)? '))
except ValueError:
    print("Invalid input. Please enter numbers.")
    exit()

# Variable transformation function (maps interval [a, b] to [-1, 1])
def Ft(t):
    return f(((b - a) * t + (b + a)) / 2)

integral_value = None

if G == 2:
    w1, w2 = 1, 1
    t1, t2 = -1/math.sqrt(3), 1/math.sqrt(3)
    integral_value = ((b - a) / 2) * (w1 * Ft(t1) + w2 * Ft(t2))

elif G == 3:
    w1, w2, w3 = 5/9, 8/9, 5/9
    t1, t2, t3 = -math.sqrt(3/5), 0, math.sqrt(3/5)
    integral_value = ((b - a) / 2) * (w1 * Ft(t1) + w2 * Ft(t2) + w3 * Ft(t3))

elif G == 4:
    w1, w2, w3, w4 = 0.3478548, 0.6521452, 0.6521452, 0.3478548
    t1, t2, t3, t4 = -0.86113631, -0.33998104, 0.33998104, 0.86113631
    integral_value = ((b - a) / 2) * (w1 * Ft(t1) + w2 * Ft(t2) + w3 * Ft(t3) + w4 * Ft(t4))

elif G == 5:
    w1, w2, w3, w4, w5 = 0.2369269, 0.4786287, 0.568889, 0.4786287, 0.2369269
    t1, t2, t3, t4, t5 = -0.90617985, -0.53846931, 0, 0.53846931, 0.90617985
    integral_value = ((b - a) / 2) * (w1 * Ft(t1) + w2 * Ft(t2) + w3 * Ft(t3) + w4 * Ft(t4) + w5 * Ft(t5))

elif G == 6:
    w1, w2, w3, w4, w5, w6 = 0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245
    t1, t2, t3, t4, t5, t6 = -0.93246951, -0.66120938, -0.23861919, 0.23861919, 0.66120938, 0.93246951
    integral_value = ((b - a) / 2) * (w1 * Ft(t1) + w2 * Ft(t2) + w3 * Ft(t3) + w4 * Ft(t4) + w5 * Ft(t5) + w6 * Ft(t6))

else:
    print('Formula not available')

# Final Output
if integral_value is not None:
    print(f'The value of integration is {integral_value:.6f}')
