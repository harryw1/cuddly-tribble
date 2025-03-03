import numpy as np
import codecademylib3
from math import sin, cos, log, pi
import matplotlib.pyplot as plt


def limit_derivative(f, x, h):
    """Return the derivative of f at x using the limit definition of derivative.

    f: function to be differentiated
    x: the point at which to differentiate f
    h: distance between the points to be evaluated
    """
    # compute the derivative at x with limit definition
    return (f(x + h) - f(x)) / h


# f1(x) = sin(x)
def f1(x):
    return sin(x)


# f2(x) = x^4
def f2(x):
    return pow(x, 4)


# f3(x) = x^2*log(x)
def f3(x):
    return pow(x, 2) * log(x)


# Calculate derivatives here
print(limit_derivative(f3, 1, 2))
print(limit_derivative(f3, 1, 0.1))
print(limit_derivative(f3, 1, 0.00001))


# Graph the true derivative
x_vals = np.linspace(1, 10, 200)
# y_vals = [cos(val) for val in x_vals]
y_vals = [4 * pow(val, 3) for val in x_vals]
plt.figure(1)
plt.plot(x_vals, y_vals, label="True Derivative", linewidth=4)


# plot different approximated derivatives of f using limit definition of derivative
def plot_approx_deriv(f):
    """Plot approximated derivatives of function f using the limit definition of derivative with various h values.

    Args:
        f: function to be differentiated

    Returns:
        None. Displays a plot showing how derivative approximations converge as h decreases.

    """
    x_vals = np.linspace(1, 10, 200)
    h_vals = [10, 1, 0.25, 0.01]

    for h in h_vals:
        derivative_values = []
        for x in x_vals:
            derivative_values.append(limit_derivative(f, x, h))
        plt.plot(x_vals, derivative_values, linestyle="--", label="h=" + str(h))
    plt.legend()
    plt.title("Convergence to Derivative by varying h")
    plt.show()


# Plot here
# plot_approx_deriv(f1)
plot_approx_deriv(f2)
