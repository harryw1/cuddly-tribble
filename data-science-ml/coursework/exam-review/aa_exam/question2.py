import numpy as np
## I am mad at codecademy. This is linear algebra
## and was never covered in the course.

# Given
"""
3x + z = 8
y - z - 2x = 3
z + 4x - y = 5
"""

# Define A
A = np.array([[3, 0, 1], [-2, 1, -1], [4, -1, 1]])

# Define b
b = np.array([8, 3, 5])

# Calculate x,y,z
x, y, z = np.linalg.solve(A, b)

# Print x,y,z
print(x, y, z)
