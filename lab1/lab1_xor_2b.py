import numpy as np


def lab1_xor_2b(x0: float, y0: float) -> dict:
    """
Funkcja, która wykonuje operację logiczną 'XOR' wg pkt 2b na dwóch liczbach.
    :rtype: dict
    :param x0: Współrzędna 'x' punktu.
    :param y0: Współrzędna 'y' punktu.
    :return: Odpowiednie wagi i progi.
    """
    point = np.array([[x0], [y0]])

    # Przygotujmy wektor na odpowiedzi dwóch perceptronów prostych
    out_lines = np.array([[0], [0]])

    # Równania prosych Ax + By + C = 0
    A1, B1, C1 = -2, -2, 1
    A2, B2, C2 = -2, -2, 3

    # Sprawdzamy, czy punkt x0, y0 leży ponad prostą 1
    # Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B
    # Dzielenie przez B jest istotne, gdyż nie znając jego znaku, przy ujemnym nierówność zmienia stronę
    weights_line1 = np.array([[A1 / B1, B1 / B1]])
    threshold_line1 = -C1 / B1

    # Sprawdzamy, czy punkt x0, y0 leży pod prostą 2
    # Skoro znak perceptronu jest '>=', a chcemy sprawdzić, czy jest pod linią '<',
    # musimy przemnożyć wagi oraz próg przez '-1'
    weights_line2 = -np.array([[A2 / B2, B2 / B2]])
    threshold_line2 = C2 / B2

    # Parametry perceptronu wyjścia
    weights_out = np.array([[1, 1]])  # Równa waga dla obu prostych
    threshold_out = 2  # Oba warunki spełnione

    # Obliczanie wyjść perceptronów
    out_lines[0] = 1 if (np.dot(weights_line1, point)) >= threshold_line1 else 0
    out_lines[1] = 1 if (np.dot(weights_line2, point)) >= threshold_line2 else 0

    # Perceptron wyjścia
    out = 1 if (np.dot(weights_out, out_lines)) >= threshold_out else 0

    print(f'{point[0][0]} XOR 2b {point[1][0]}: {out}')

    # Dictionary do zapisu w JSON
    network = {
        'input': {
            1: {
                'weights': [float(weights_line1[0][0]), float(weights_line1[0][1])], 'threshold': threshold_line1
            },
            2: {
                'weights': [float(weights_line2[0][0]), float(weights_line2[0][1])], 'threshold': threshold_line2
            }
        },
        'hidden': dict(),
        'output': {
            1: {
                'weights': [float(weights_out[0][0]), float(weights_out[0][1])], 'threshold': threshold_out
            }
        }
    }

    return network
