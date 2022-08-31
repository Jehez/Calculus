#importing matplotlib for graphing
#only 4 functions have been imported to save time
from matplotlib.pyplot import plot,show,grid,legend

#defining f(x)
#Note- n has been used to avoid global and local variable interference
def f(n):
    return n*n

#defining f_dash(x); it uses δy/δx
def f_dash(n):
    δx = 0.01   #small change
    δy = f(n+δx)-f(n)   #calculating δy
    return δy/δx        #returning δy/δx (approximately dy/dx)

#a function which has to be made manually, it displays the actual dy/dx value (here x**2 differentiated would be 2x)
#I am using it to compare between accuracy of δy/δx and dy/dx
def dydx(n):
    return 2*n

#starting and ending values
start = 0
end = 100

#precision for changing x while calculating values
prec = 0.1

#arrays for storing x-axis,y-axis and gradient values
x_axis = []
y_axis = []
gradient = []

#making an array to store the difference between dy/dx and δy/δx
deviation = []

#using while loop for non-integer precision
x = start
while x<=end:
    x_axis.append(x)
    y_axis.append(f(x))
    approx = f_dash(x)
    exact = dydx(x)
    gradient.append(approx)
    deviation.append(abs(exact-approx))
    x+=prec

#calculating deviations
#results are displayed till 4 decimal places
print("Maximum deviation:\t{:.4f}".format(max(deviation)))
print("Minimum deviation:\t{:.4f}".format(min(deviation)))
print("Average deviation:\t{:.4f}".format(sum(deviation)/len(deviation)))

#graphing part
plot(x_axis,y_axis,label='f(x)')     #plotting f(x)
plot(x_axis,gradient,label='f\'(x)')   #plotting f'(x)
grid()
legend(loc='upper right')
show()