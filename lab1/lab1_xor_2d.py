import numpy as np


def lab1_xor_2d(x0: float, y0: float) -> dict:
    """
Funkcja, która wykonuje operację logiczną 'XOR' wg pkt 2d na dwóch liczbach,
bez wykorzystania nadmiarowej instrukcji 'if'.
    :rtype: dict
    :param x0: Współrzędna 'x' punktu.
    :param y0: Współrzędna 'y' punktu.
    :return: Odpowiednie wagi i progi.
    """
    point = np.array([[x0], [y0]])

    # Założenie jest takie, że od instrukcji 'OR' odejmiemy 'AND' i wyjdzie 'XOR'
    # Założenie wykonane przy użyciu jednej ukrytej warstwy perceptronów

    # Przygotujmy wektor na odpowiedzi dwóch perceptronów prostych i warstwy ukrytej
    out_lines = np.array([[0], [0]])
    out_hidden = np.array([[0], [0]])

    # Równania prostych Ax + By + C = 0
    A1, B1, C1 = 2, 0, -1
    A2, B2, C2 = 0, 2, -1

    # Perceptron wejściowy 1
    # Po przekształceniu x0 - x(y0) = 0 -> Ax0/A + By0/A = -C/A -> sprawdzanie lewo/prawo
    weights_line_v = np.array([[A1 / A1, B1 / A1]])
    threshold_line_v = -C1 / A1

    # Perceptron wejściowy 2
    # Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B -> sprawdzanie góra/dół
    weights_line_h = np.array([[A2 / B2, B2 / B2]])
    threshold_line_h = -C2 / B2

    # Perceptron warstwy ukrytej 1
    # Jego celem jest wykrywanie OR
    weights_hidden_or = np.array([[1, 1]])
    threshold_hidden_or = 1  # Wykrywa albo góra, albo prawo

    # Perceptron warstwy ukrytej 2
    # Jego celem jest wykrywanie AND
    weights_hidden_and = np.array([[1, 1]])
    threshold_hidden_and = 2  # Wykryrwa góra oraz prawo

    # Perceptron wyjściowy
    weights_out = np.array([[1, -1]])  # XOR jest kiedy jest OR, ale nie ma AND
    threshold_out = 1

    # Najpierw sprawdź, czy jest na prawo od pionowej i ponad poziomą prostą
    out_lines[0] = 1 if np.dot(weights_line_v, point) >= threshold_line_v else 0  # Wykryte prawo
    out_lines[1] = 1 if np.dot(weights_line_h, point) >= threshold_line_h else 0  # Wykryta góra

    # Wykorzystaj te informacje, by określić OR i AND
    out_hidden[0] = 1 if np.dot(weights_hidden_or, out_lines) >= threshold_hidden_or else 0  # OR
    out_hidden[1] = 1 if np.dot(weights_hidden_and, out_lines) >= threshold_hidden_and else 0  # AND

    # Sprawdź, czy jest OR, ale nie ma AND
    out = 1 if np.dot(weights_out, out_hidden) >= threshold_out else 0

    print(f'{point[0][0]} XOR 2d {point[1][0]}: {out}')

    # Dictionary do zapisu w JSON
    network = {
        'input': {
            1: {
                'weights': [float(weights_line_v[0][0]), float(weights_line_v[0][1])], 'threshold': threshold_line_v
            },
            2: {
                'weights': [float(weights_line_h[0][0]), float(weights_line_h[0][1])], 'threshold': threshold_line_h
            }
        },
        'hidden': {
            1: {
                'weights': [float(weights_hidden_or[0][0]), float(weights_hidden_or[0][1])], 'threshold': threshold_hidden_or
            },
            2: {
                'weights': [float(weights_hidden_and[0][0]), float(weights_hidden_and[0][1])], 'threshold': threshold_hidden_and
            }
        },
        'output': {
            1: {
                'weights': [float(weights_out[0][0]), float(weights_out[0][1])], 'threshold': threshold_out
            }
        }
    }

    return network
