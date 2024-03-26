import numpy as np
from comparison import comparison

np.random.seed(10)
n_points = 10
x_points = np.linspace(-10, 10, 500)
x_uniform = np.linspace(-10, 10, n_points)

functions = [
    {'func': lambda x: 2 * x + 3, 'label': 'Linear'},
    {'func': lambda x: 0.1 * x ** 2 - 1 * x + 2, 'label': 'Quadratic'},
    {'func': lambda x: 0.1 * x ** 2 - 1 * x + 2, 'label': 'Quadratic'},
    {'func': lambda x: 5 * np.sin(x), 'label': 'Sine'},
    {'func': lambda x: np.exp(0.2 * x), 'label': 'Exponential'}
]

data_sets = []
for func_info in functions:
    data_uniform = [[x, func_info['func'](x)] for x in x_uniform]
    x_clustered = np.concatenate((np.linspace(-10, -6, 2), np.linspace(-4, 4, 6), np.linspace(6, 10, 2)))
    data_clustered = [[x, func_info['func'](x)] for x in x_clustered]
    x_random = np.sort(np.random.choice(x_points, n_points, replace=False))
    data_random = [[x, func_info['func'](x)] for x in x_random]
    data_sets.append({
        'uniform': data_uniform,
        'clustered': data_clustered,
        'random': data_random,
        'func_info': func_info
    })

for data_set in data_sets:
    for key in ['uniform', 'clustered', 'random']:
        current_data = data_set[key]
        original_func = data_set['func_info']['func']
        print(f"Comparison for {data_set['func_info']['label']} ({key} density) :")
        comparison(current_data, 5)
        print('\n' + '-' * 80 + '\n')