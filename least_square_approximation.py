import numpy as np

def least_square_approximation(data, degree):
    data = sorted(data, key=lambda item: item[0])
    x = np.array([point[0] for point in data])
    y = np.array([point[1] for point in data])
    coefficients = np.polyfit(x, y, degree)
    polynomial = np.poly1d(coefficients)
    return polynomial

