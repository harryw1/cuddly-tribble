import numpy as np

a = np.array([2, -3, 1])
b = np.array([3, 1, 1])
c = np.array([-1, -2, -1])
d = np.array([2, -1, 1])
A = np.column_stack((a, b, c))
print(np.linalg.solve(A, d))


def unit_vector(vector):
    """Return the unit vector of the vector."""
    return vector / np.linalg.norm(vector)


def angle_between(v1, v2):
    """Return the angle in radians between vectors.

    >>> angle_between((1, 0, 0), (0, 1, 0))
    1.5707963267948966
    >>> angle_between((1, 0, 0), (1, 0, 0))
    0.0
    >>> angle_between((1, 0, 0), (-1, 0, 0))
    3.141592653589793
    """
    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    return np.arccos(np.clip(np.dot(v1_u, v2_u), -1.0, 1.0))


a = np.array([3, -1, 2])
b = np.array([0, -1, 1])
print(np.rad2deg(angle_between(a, b)))

a = np.array([[2, -3, 1], [-2, -1, 4], [0, 2, 2]])
b = np.array([[3, -2, 1], [1, -1, 2], [-2, 2, 0]])
print(np.dot(a, b))
