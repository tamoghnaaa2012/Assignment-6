#Question 4



from mylib import *
import math
import random


file = open("data_Q4.dat", "w+")


def f(x):
    return (4/(1 + (x**2)))



#limits(a,b) and no of random values
a = 0
b = 1
N = 100000

#calling function
result = monte_carlo(a, b, f, N,file)
print("Integration of the function and sigma_value= ", result)



"""
Integration of the function and sigma_value=  (3.1444636704989817, 0.6428447110673978)

Process finished with exit code 0


"""