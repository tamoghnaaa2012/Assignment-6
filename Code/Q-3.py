#Question-3



from mylib import *
import math

def f(x):
    e=2.718281828459045
    return e**(-x**2)



def g(x):                                   #g(x) is defined as second derivative of the function f(x)
    e=2.718281828459045
    return (((4*x**2)-2)*e**(-x**2))


def h(x):                                     ##h(x) is defined as fourth derivative of the function f(x)
    e=2.718281828459045
    return (8*x**2)-(32*x*e**(-x**2))+((((4*x**2)-2)**2)*e**(-x**2))



def error_midpoint(g,a,b):                                 #Error related function for Midpoint method
    err = ((((b-a)**3)/(24*0.001))*abs(g(0)))**0.5
    return math.ceil(err)



def error_trapezoid(g,a,b):                                 #Error related function for Trapezoidal method
    err = ((((b-a)**3)/(12*0.001))*abs(g(0)))**0.5
    return math.ceil(err)


def error_simpson(h,a,b):                                   #Error related function for Simpson method
    err = ((((b-a)**5)/(180*0.001))*abs(h(0)))**0.25
    return math.ceil(err)








n= error_midpoint(g,0,1)
print("The value of N for midpoint method",n)
ans = midpoint(f,0,1,n)
print("The Integral value",ans)


print()


n1= error_trapezoid(g,0,1)
print("The value of N for trapezoidal method",n1)
ans1 = trapezoid(f,0,1,n)
print("The Integral value",ans1)


print()


n2= error_simpson(h,0,1)
print("For simpson method N =",n2)
print("There is a problem for odd N,so we will take N=4")
ans3 = simpson(f,0,1,(n2+1))
print("The Integral value",ans3)




"""

The value of N for midpoint method 10
The Integral value 0.7471308777479975

The value of N for trapezoidal method 13
The Integral value 0.7462107961317495

For simpson method N = 3
There is a problem for odd N,so we will take N=4
The Integral value 0.7468553797909873

Process finished with exit code 0



"""