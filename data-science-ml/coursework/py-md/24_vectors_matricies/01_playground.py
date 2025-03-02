import numpy as np
from scipy.linalg import lu


def magnitude(x):
    """Return the magnitude of a vector x."""
    return np.sqrt(np.sum(x**2))


def deg_between(x, y):
    """Return the angle in degrees between vectors x and y."""
    return np.arccos(np.dot(x, y) / (magnitude(x) * magnitude(y))) * 180 / np.pi


if __name__ == "__main__":
    x = np.array([2, 3, 0, 5, 1])
    print(magnitude(x) ** 2)

    y = np.array([3, -1, 2])
    z = np.array([0, -1, 1])
    print(np.round(deg_between(y, z), 0))

    a = np.array([[2, -3, 1], [-2, -1, 4], [0, 2, 2]])
    b = np.array([[3, -2, 1], [1, -1, 2], [-2, 2, 0]])
    print(np.dot(a, b))

    A = np.array([[2, -3, 1], [3, 1, 1], [-1, -2, -1]])
    b = np.array([2, -1, 1])

    x, y, z = np.linalg.solve(A, b)
    print(x, y, z)
