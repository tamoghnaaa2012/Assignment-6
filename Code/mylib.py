#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
import random




def midpoint(f, a, b, n): 
    h = float(b-a)/n                          #finding midpoint
    result = 0
    
    for i in range(n):
        result += f((a + h/2.0)) 
        a += h
    result *= h                               #multiplying with the midpoint
    return result





def trapezoid(f, a, b, n):
    h = (b-a)/float(n) #finding midpoint
    result = f(a) + f(b)  

    for i in range(1,n,1):
        result = result + (2*(f(a + i*h))) #finding 2*f(x)
    result *= (h/2.0) #multiplying with dx/2.0

    return result






def simpson(f, a, b, n):
    h = (b-a)/float(n)
    result = f(a) + f(b)

    for i in range(1,n,1):
        if(i%2 ==0):
            result = result + (2*(f(a + i*h)))
        else:
            result = result + (4*(f(a + i*h)))
    result *= (h/3.0)

    return result






def monte_carlo(a, b, f, N,file):
    Fn = 0
    sum_fx = 0
    square_sum_fx=0
    
    for i in range(N):
        x = random.random()
        x = a + ((b - a)*x)
        fx = f(x)
        sum_fx = sum_fx + fx
        Fn = ((b - a)/(i+1)) * sum_fx
        
        square_sum_fx += (fx)**2
        variance=(square_sum_fx /N) - (sum_fx /N)**2
        sigma = math.sqrt(variance)
        
        file.write("{:<15}{:<20}\n".format((i+1), Fn))
    file.close()
    return Fn ,sigma

