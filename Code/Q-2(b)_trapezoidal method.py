#Question-2(b)-   for Trapezoidal method


from mylib import *

def f(x):
    return x/(x+1)



print("For Trapezoidal method")

print("N","     ","Result","                 ","Analytical value")
trapezoidal_5 = trapezoid(f,1,3,5)
print("5","     ",trapezoidal_5, "      ","1.306852819440055")

trapezoidal_10 = trapezoid(f,1,3,10)
print("10","    ",trapezoidal_10, "      ","1.306852819440055")

trapezoidal_15 = trapezoid(f,1,3,15)
print("15","    ",trapezoidal_15, "      ","1.306852819440055")





"""
For Trapezoidal method
N       Result                   Analytical value
5       1.3043650793650796        1.306852819440055
10      1.3062285968245722        1.306852819440055
15      1.3065751956419356        1.306852819440055

Process finished with exit code 0

"""