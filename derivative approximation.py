# Approximating derivatives

# A derivative is defined as the following limit:
# f(x+δx)-f(x) over δx as δx approaches 0
# which may be rephrased as 
# δy/δx as δx approaches 0
# setting f(x+δx)-f(x) as δy

# Using this, we can use 2 values of x which have δx (x2-x1) as a very small number

#defining the function we want to differentiate
def f(n):
    return n**3-2*n**2+n+4

#x for which we want the derivative of f(x)
x = 5
δx = 10**-8 #small change

#actual calculations of δy
x1 = x
x2 = x1+δx

δy = f(x2)-f(x1)

print(f"Derivative at x={x} is:\t{δy/δx}")
