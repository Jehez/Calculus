# Approximating Integrals (Definite)

# Integrals are used to find the area under a curve
# The area under the curve can be approximated as
# the sum of areas of several trapeziums from x to x+δx

# Sides of trapezium: f(x), f(x+δx)
# Height of trapezium: δx

#defining the function we want to integrate
def f(n):
    return n**3-2*n**2+n+4

a = -2   #bounds
b = 0

prec = 10**-2   #precision or δx (not very small for faster calculations)
δx = prec

x = a

total_area = 0

while x<b:
    s1 = f(x)
    s2 = f(x+δx)
    h = δx
    area = h*(s1+s2)/2
    total_area+=area
    x+=prec

print(total_area)