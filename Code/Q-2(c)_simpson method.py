#Question-2(c)-   for Simpson method


from mylib import *

def f(x):
    return x/(x+1)




print("For Simpson method")

print("N","       ","Result","                 ","Analytical value")
simpson_6 = simpson(f,1,3,6)
print("6","      ",simpson_6, "      ","1.306852819440055")

simpson_10 = simpson(f,1,3,10)
print("10","     ",simpson_10, "      ","1.306852819440055")

simpson_16 = simpson(f,1,3,16)
print("16","     ",simpson_16, "      ","1.306852819440055")




"""
For Simpson method
N         Result                   Analytical value
6        1.3068302068302067        1.306852819440055
10       1.3068497693110694        1.306852819440055
16       1.3068523471805809        1.306852819440055

Process finished with exit code 0


"""