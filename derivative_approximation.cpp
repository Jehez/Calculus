#include <iostream>

// A derivative is defined as the following limit:
// f(x+delta_x)-f(x) / delta_x as delta_x approaches 0
// This can be rewritten as delta_y/delta_x as delta_x approaches 0 by setting f(x+delta_x)-f(x) as delta_y

// In computation, we cannot actually set delta_x to 0 as division by 0 is not possible
// delta_x can only approach 0, or become infinitesimally small

// As this program is aimed at precision, we will use long double
// For demonstration, a simple polynomial is used: f(x) = x^3-x^2-x called 'y'

long double y(long double x) {
    return x*x*x-x*x-x;
}

long double derivative_approximation(long double x, long double delta_x, long double (*func)(long double)) {
    return (func(x+delta_x)-func(x))/delta_x;
}

int main() {
    long double result = derivative_approximation(2,0.0001,y);
    std::cout << result;
    return 0;
}

// Time complexity:
// The only computation done is the function 'y' being called - the function from which to obtain the derivative of
// The time complexity of the function is same as the time_complexity of y

// Space complexity:
// no variables are being stored directly so space complexity is O(1)