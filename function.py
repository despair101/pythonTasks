from math import *

def Foo(x):
    return abs(sin(sqrt(x + 1)) / sqrt(x**2 + 4 * x + 6))

arg, end, eps = 1, 2, 1e-9
while arg <= end + eps:
    print("y(", '%.1f' % arg,") = ", round(Foo(arg), 2), sep = '')
    arg += 0.1
