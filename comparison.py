from find_best_approximation import find_best_approximation
from least_square_approximation import least_square_approximation
import numpy as np
import matplotlib.pyplot as plt

def comparison(data, degree):
    result_poly_a = find_best_approximation(data, degree)
    result_poly_b = least_square_approximation(data, degree)

    data = sorted(data, key=lambda item: item[0])
    x = np.array([point[0] for point in data])
    y = np.array([point[1] for point in data])
    x_poly = np.linspace(x[0], x[-1], 100)
    y_poly_a = result_poly_a(x_poly)
    y_poly_b = result_poly_b(x_poly)


    plt.scatter(x, y, label='Original data')
    plt.plot(x_poly, y_poly_a, label='Approximation by new method')
    plt.plot(x_poly, y_poly_b, label='Approximation by least-squares')

    plt.legend()
    plt.title('Comparison: Least-squares vs. New Method')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)
    plt.show()

    sqr_error_a = [(result_poly_a(point[0]) - point[1]) ** 2 for point in data]
    sqr_error_b = [(result_poly_b(point[0]) - point[1]) ** 2 for point in data]
    average_sqr_error_a = np.mean(sqr_error_a)
    average_sqr_error_b = np.mean(sqr_error_b)
    difference = abs(average_sqr_error_a - average_sqr_error_b)

    print('Average squared error by new method:', average_sqr_error_a)
    print('Average squared error by least-squares:', average_sqr_error_b)
    if average_sqr_error_a < average_sqr_error_b:
        print('New method performs better by', difference)
    elif average_sqr_error_a > average_sqr_error_b:
        print('Least-squares performs better by', difference)
    else:
        print('Both methods perform equally. No difference in average squared error.')

    return difference