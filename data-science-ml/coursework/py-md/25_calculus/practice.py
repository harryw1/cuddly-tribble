import sympy as sp

x = sp.symbols("x")
f = 2 * sp.ln(x) - 6
limit = sp.limit(f, x, 1)
print(limit)

# Define the symbolic variable x
x = sp.symbols('x')

# Define the function f(x) = 2x**4 + e**x - sin(x)
f_x = 2*x**4 + sp.exp(x) - sp.sin(x)

# Calculate the derivative of f(x) with respect to x
derivative_f_x = sp.diff(f_x, x)

# Print the derivative
print(derivative_f_x)