import sympy as sp
import itertools

def find_best_approximation(data, degree):

    def polynomial_approximation(selected_points, degree):
        symbol_names = ' '.join([f'c{i}' for i in range(degree + 1)]) + ' A'
        symbols = sp.symbols(symbol_names)
        equations = []
        for i in range(degree + 2):
            eq = selected_points[i][1]
            for j in range(degree + 1):
                eq -= symbols[j] * (selected_points[i][0] ** j)
            equation = sp.Eq(symbols[-1] * (-1) ** i, eq)
            equations.append(equation)
        solutions = sp.solve(equations, symbols)

        def poly(x):
            predicted_y = 0
            for k in range(degree + 1):
                predicted_y += solutions[symbols[k]] * (x ** k)
            return predicted_y

        return poly, solutions[symbols[-1]]


    data = sorted(data, key=lambda item: item[0])

    result = []

    combinations = list(itertools.combinations(data, degree + 2))
    for combination in combinations:
        selected_points = sorted(combination, key=lambda item: item[0])
        result_poly, A = polynomial_approximation(selected_points, degree)
        num = 0
        for j in range(len(data)):
            error = abs(data[j][1] - result_poly(data[j][0]))
            if abs(A) + 0.001 < error:
                num += 1
        if num == 0:
            result_element = []
            result_element.append(result_poly)
            result_element.append(abs(A))
            result.append(result_element)

    result = sorted(result, key=lambda item: item[1])

    return result[0][0]