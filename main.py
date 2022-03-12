import numpy as np

# Zadanie 1

# Wartość zadana
in_val = [[1], [1]]
xor_y = np.array([[0], [0]])

# Współczynniki równań prostych
xor_param1, xor_param2 = np.array([[2, -2]]), np.array([[2, -2]])
xor_b1, xor_b2 = -1, 1

# Parametry perceptronu wyjścia
xor_yparam = np.array([[1, 1]])
xor_yb = 1

# Obliczanie wyjść perceptronów
xor_y[0] = 1 if (np.dot(xor_param1, in_val)) < xor_b1 else 0
xor_y[1] = 1 if (np.dot(xor_param2, in_val)) > xor_b2 else 0

# Perceptron wyjścia
xor_out = 1 if (np.dot(xor_yparam, xor_y)) >= xor_yb else 0

print(f'{in_val[0]} XOR 2c {in_val[1]}: {xor_out}')

# Zadanie 2
and_param = np.array([[-2, -2]])
and_b = 3

and_out = 1 if (np.dot(and_param, in_val)) < -and_b else 0

print(f'{in_val[0]} AND {in_val[1]}: {and_out}')

# Zadanie 3
xor_y = np.array([[0], [0]])

xor_param1, xor_param2 = np.array([[-1, -1]]), np.array([[-1, -1]])
xor_b1, xor_b2 = 1.5, 0.5

xor_yparam = np.array([[1, 1]])
xor_yb = 1

xor_y[0] = 1 if (np.dot(xor_param1, in_val)) > -xor_b1 else 0
xor_y[1] = 1 if (np.dot(xor_param2, in_val)) < -xor_b2 else 0

xor_out = 1 if (np.dot(xor_yparam, xor_y)) >= xor_yb else 0

print(f'{in_val[0]} XOR 2b {in_val[1]}: {xor_out}')
