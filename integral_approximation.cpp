#include <iostream>

// the method used in this program will be the trapezoidal rule
// the area of a trapezium is (s1+s2)*h/2 where s1,s2 are parallel sides and h is the perpendicular distance between the 2 (the height)
// On a curve, a trapezium an be made with 2 lines, perpendicular to the x-axis, intersecting the curve
// If the lines are very close together, the trapzeium area will be very close to the actual area under the curve

// These lines need to have an infinitesimally small - usually represented as dx
// As we can't compute with dx, we will instead use delta_x

// For the trapezium formed with lines some value x and x+delta_x:
// s1 and s2 will be f(x) and f(x+delta_x) - the corresponding y-values where the lines intersect the curve
// h will be delta_x
// Hence, the final area will be (f(x)+f(x+delta_x))*delta_x/2

// As this program is aimed at precision, we will use long double
// For demonstration, a simple polynomial is used: f(x) = x^3-x^2-x called 'y'

long double y(long double x) {
    return x*x*x-x*x-x;
}

long double integral_approximation(long double lower_bound, long double upper_bound, long double delta_x, long double (*func)(long double)) {
    long double area = 0;
    for (long double x = lower_bound; x<upper_bound; x+=delta_x){area += (func(x)+func(x+delta_x))*delta_x/2;}
    return area;
}

int main() {
    long double result = integral_approximation(-1,2,0.01,y);
    std::cout << result;
    return 0;
}

// Time complexity:
// The value of x ranges from upper_bound-lower_bound and the number of iterations needed will increase as delta_x decreases
// In each iteration, the function which is being integrated 'y' is called twice
// The expression obtained is O( (upper_bound-lower_bound)*(time_complexity of y)/delta_x )

// Space complexity:
// Only 1 variable is being stored - area so space complexity is O(1)