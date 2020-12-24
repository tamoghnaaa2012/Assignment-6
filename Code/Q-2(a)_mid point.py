#Question-2(a)-   for Mid-point method

from mylib import *



def f(x):
    return x/(x+1)



print("For Mid-point method")
print("N","     ","Result","                ","Analytical value")
midpoint_5 = midpoint(f,1,3,5)
print("5","    ",midpoint_5, "      ","1.306852819440055")

midpoint_10 = midpoint(f,1,3,10)
print("10","   ",midpoint_10, "     ","1.306852819440055")

midpoint_15 = midpoint(f,1,3,15)
print("15","   ",midpoint_15, "     ","1.306852819440055")



"""

For Mid-point method
N       Result                  Analytical value
5      1.308092114284065        1.306852819440055
10     1.3071646395900398       1.306852819440055
15     1.3069915736287043       1.306852819440055

Process finished with exit code 0


"""