import numpy as np


def lab1_and(x0: float, y0: float) -> dict:
    """
Funkcja, która wykonuje operację logiczną 'AND' na dwóch liczbach.
    :rtype: dict
    :param x0: Współrzędna 'x' punktu.
    :param y0: Współrzędna 'y' punktu.
    :return: Odpowiednie wagi i progi.
    """
    point = np.array([[x0], [y0]])

    # Równanie prostej Ax + By + C = 0
    A, B, C = -2, -2, 3

    # Sprawdzamy, czy punkt x0, y0 leży ponad prostą
    # Po przekształceniu y0 - y(x0) >= 0 -> Ax0/B + By0/B >= -C/B
    # Dzielenie przez B jest istotne, gdyż nie znając jego znaku, przy ujemnym nierówność zmienia stronę
    weights = np.array([[A/B, B/B]])
    threshold = -C/B

    # Perceptron wejścia/wyjścia
    out = 1 if (np.dot(weights, point)) >= threshold else 0

    print(f'{point[0][0]} AND {point[1][0]}: {out}')

    # Dictionary do zapisu w JSON
    network = {
        'input': {
            1: {
                'weights': [float(weights[0][0]), float(weights[0][1])], 'threshold': threshold
            }
        },
        'hidden': dict(),
        'output': dict()
    }

    return network
