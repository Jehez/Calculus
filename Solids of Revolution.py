from math import pi
# Volume (Solids of Revolution)

# Volume after revolution = pi * integral from a to b (y^2 dx)
# Here, y will be f(x) so we will integrate f(x)^2 dx

def f(x):
    return (1-x*x)**0.5 #equation of a circle with radius 1 here (above x axis)

precision = 0.001 #increments in x
δx = precision #delta x: small value as it approaches 0

# the method used here with a trapezium is the same as the one used in "Integral Approximation"
a,b = 0,1   #setting of limits a and b

x = a
total = 0

while x+δx<b:   #the +δx is added to avoid any errors which may occur due to x+δx surpassing b such as complex numbers (the error is negligible but is still presented in the answer)
    s1 = f(x)**2
    s2 = f(x+δx)**2
    if s1.imag or s2.imag:  print(x)
    h = δx
    total += h*(s1+s2)/2
    x+=precision

total*=pi