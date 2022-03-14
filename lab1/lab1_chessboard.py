import numpy as np


def lab1_chessboard(x0: float, y0: float) -> dict:
    """
Funkcja realizująca rozwiązanie problemu szachownicy. Wprowadzone zostały strefy
od początku układu współrzędnych co 1 jednostkę długości.
Tak więc, strefa pierwsza (X,Y): (0-1, 0-1), druga (X,Y): (1-2, 0-1) itd. aż do
(X, Y): (2-3, 2-3).
    :rtype: dict
    :param x0: Współrzędna 'x' punktu.
    :param y0: Współrzędna 'y' punktu.
    :return: Odpowiednie wagi i progi.
    """
    # 3
    #   A | B | A
    # 2---+---+---
    #   B | A | B
    # 1---+---+---
    #   A | B | A
    # 0   1   2   3

    # Współrzędne punktu:
    point = np.array([[x0], [y0]])

    # Sieć będzie posiadać cztery perceptrony wejściowe, po jednym na prostą
    # oraz dwa perceptrony warstwy ukrytej.

    # Przygotujmy wektor na odpowiedzi czterech perceptronów prostych i dwóch warstwy ukrytej
    out_lines = np.array([[0], [0], [0], [0]])
    out_hidden = np.array([[0], [0]])

    # Równania prostych Ax + By + C = 0:

    A_up, B_up, C_up = 0, 1, -2
    weights_up = np.array([[A_up / B_up, B_up / B_up]])
    threshold_up = -C_up / B_up

    #    |   |      ^
    # ---+---+---   |   Górna prosta sprawdza górę
    #    |   |
    # ---+---+---
    #    |   |

    A_down, B_down, C_down = 0, 1, -1
    weights_down = -np.array([[A_down / B_down, B_down / B_down]])
    threshold_down = C_down / B_down

    #    |   |
    # ---+---+---
    #    |   |
    # ---+---+---   |   Dolna prosta sprawdza dół - odwrócony znak
    #    |   |      v

    A_left, B_left, C_left = 1, 0, -1
    weights_left = -np.array([[A_left / A_left, B_left / A_left]])
    threshold_left = C_left / A_left

    #   <--              Lewa prosta sprawdza lewo - odwrócony znak
    #    |   |
    # ---+---+---
    #    |   |
    # ---+---+---
    #    |   |

    A_right, B_right, C_right = 1, 0, -2
    weights_right = np.array([[A_right / A_right, B_right / A_right]])
    threshold_right = -C_right / A_right

    #        -->         Prawa prosta sprawdza prawo
    #    |   |
    # ---+---+---
    #    |   |
    # ---+---+---
    #    |   |

    # Zasada działania:
    # Jeżeli punkt jest wykryty przez 2 perceptrony (np. GÓRA, PRAWO), jest z grupy A
    # Jeżeli punkt jest wykryty przez TYLKO 1 perceptron (np. GÓRA), jest z grupy B
    # Jeżeli punkt nie jest wykryty przez żaden perceptron, jest z grupy A

    # Warstwa ukryta ma za zadanie odsiewać 2 wykrycia od 1 wykrycia
    weights_hidden = np.array([1, 1, 1, 1])
    threshold_hidden1 = 1
    threshold_hidden2 = 2

    # Perceptron wyjścia wskazuje TRUE, gdy punkt należy do A, oraz FALSE, gdy punkt należy do B
    weights_out = np.array([1, -1])
    threshold_out = 0

    # Perceptrony warstwy wejściowej
    out_lines[0] = 1 if np.dot(weights_up, point) >= threshold_up else 0  # Wykryta góra
    out_lines[1] = 1 if np.dot(weights_down, point) >= threshold_down else 0  # Wykryty dół
    out_lines[2] = 1 if np.dot(weights_left, point) >= threshold_left else 0  # Wykryte lewo
    out_lines[3] = 1 if np.dot(weights_right, point) >= threshold_right else 0  # Wykryte prawo

    # Perceptrony warstwy ukrytej
    out_hidden[0] = 1 if np.dot(weights_hidden, out_lines) >= threshold_hidden2 else 0  # Wykryte 2 detekcje
    out_hidden[1] = 1 if np.dot(weights_hidden, out_lines) >= threshold_hidden1 else 0  # Wykryta 1 detekcja

    # Perceptron wyjścia
    out = 1 if np.dot(weights_out, out_hidden) >= threshold_out else 0  # TRUE oznacza A, FALSE oznacza B

    print(f'Punkt x0 = {point[0][0]}, y0 = {point[1][0]} należy do zbioru {"A" if out else "B"}')

    # Dictionary do zapisu w JSON
    network = {
        'input': {
            1: {
                'weights': [float(weights_up[0][0]),
                            float(weights_up[0][1])],
                'threshold': threshold_up
            },
            2: {
                'weights': [float(weights_down[0][0]),
                            float(weights_down[0][1])],
                'threshold': threshold_down
            },
            3: {
                'weights': [float(weights_left[0][0]),
                            float(weights_left[0][1])],
                'threshold': threshold_left
            },
            4: {
                'weights': [float(weights_right[0][0]),
                            float(weights_right[0][1])],
                'threshold': threshold_right
            }
        },
        'hidden': {
            1: {
                'weights': [float(weights_hidden[0]),
                            float(weights_hidden[1]),
                            float(weights_hidden[2]),
                            float(weights_hidden[3])],
                'threshold': threshold_hidden2
            },
            2: {
                'weights': [float(weights_hidden[0]),
                            float(weights_hidden[1]),
                            float(weights_hidden[2]),
                            float(weights_hidden[3])],
                'threshold': threshold_hidden1
            }
        },
        'output': {
            1: {
                'weights': [float(weights_out[0]),
                            float(weights_out[1])],
                'threshold': threshold_out
            }
        }
    }

    return network
