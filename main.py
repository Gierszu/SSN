import numpy as np

# Wartość zadana
in_val = np.array([[1], [1]])

#####################################################
#                    PROBLEM AND                    #
#####################################################

# Równanie prostej Ax + By + C = 0
A1, B1, C1 = -2, -2, 3

# Sprawdzamy, czy punkt x0, y0 leży ponad prostą
# Po przekształceniu y0 - y(x0) >= 0 -> Ax0/B + By0/B >= -C/B
# Dzielenie przez B jest istotne, gdyż nie znamy jego znaku, przy ujemnym nierówność zmienia stronę
and_param = np.array([[A1/B1, B1/B1]])
and_b = -C1/B1

and_out = 1 if (np.dot(and_param, in_val)) >= and_b else 0

print(f'{in_val[0][0]} AND {in_val[1][0]}: {and_out}')

#####################################################
#                     PROBLEM OR                    #
#####################################################

# Równanie prostej Ax + By + C = 0
A1, B1, C1 = -2, -2, 1

# Sprawdzamy, czy punkt x0, y0 leży ponad prostą
# Po przekształceniu y0 - y(x0) >= 0 -> Ax0/B + By0/B >= -C/B
and_param = np.array([[A1/B1, B1/B1]])
and_b = -C1/B1

and_out = 1 if (np.dot(and_param, in_val)) >= and_b else 0

print(f'{in_val[0][0]} OR {in_val[1][0]}: {and_out}')

#####################################################
#                   PROBLEM XOR 2b                  #
#####################################################

# Przygotujmy wektor na odpowiedzi dwóch perceptronów prostych
xor_proste = np.array([[0], [0]])

# Równania prosych Ax + By + C = 0
A1, B1, C1 = -2, -2, 1
A2, B2, C2 = -2, -2, 3

# Sprawdzamy, czy punkt x0, y0 leży ponad prostą 1
# Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B
xor_prosta_1 = np.array([[A1 / B1, B1 / B1]])
xor_b1 = -C1/B1

# Sprawdzamy, czy punkt x0, y0 leży pod prostą 2
# Skoro znak perceptronu jest '>=', a chcemy sprawdzić, czy jest pod linią '<',
# musimy przemnożyć wagi oraz próg przez '-1'
xor_prosta_2 = -np.array([[A2 / B2, B2 / B2]])
xor_b2 = C2/B2

# Perceptron wyjściowy
xor_out_param = np.array([[1, 1]])  # Równa waga dla obu prostych
xor_outb = 2  # Oba warunki spełnione

xor_proste[0] = 1 if (np.dot(xor_prosta_1, in_val)) >= xor_b1 else 0
xor_proste[1] = 1 if (np.dot(xor_prosta_2, in_val)) >= xor_b2 else 0

xor_out = 1 if (np.dot(xor_out_param, xor_proste)) >= xor_outb else 0

print(f'{in_val[0][0]} XOR 2b {in_val[1][0]}: {xor_out}')

#####################################################
#                   PROBLEM XOR 2c                  #
#####################################################

# Przygotujmy wektor na odpowiedzi dwóch perceptronów prostych
xor_proste = np.array([[0], [0]])

# Równania prostych Ax + By + C = 0
A1, B1, C1 = 2, -2, -1
A2, B2, C2 = 2, -2, 1

# Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B

# Skoro znak perceptronu jest '>=', a chcemy sprawdzić, czy jest pod linią '<',
# musimy przemnożyć wagi oraz próg przez '-1'
xor_prosta_1 = -np.array([[A1 / B1, B1 / B1]])
xor_b1 = C1/B1

# Sprawdzamy, czy punkt x0, y0 leży ponad prostą 2
# Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B
xor_prosta_2 = np.array([[A2 / B2, B2 / B2]])
xor_b2 = -C2/B2

# Parametry perceptronu wyjścia
xor_out_param = np.array([[1, 1]])  # Równa waga warunków
xor_outb = 1  # Tylko jeden musi być spełniony

# Obliczanie wyjść perceptronów
xor_proste[0] = 1 if (np.dot(xor_prosta_1, in_val)) >= xor_b1 else 0
xor_proste[1] = 1 if (np.dot(xor_prosta_2, in_val)) >= xor_b2 else 0

# Perceptron wyjścia
xor_out = 1 if (np.dot(xor_out_param, xor_proste)) >= xor_outb else 0

print(f'{in_val[0][0]} XOR 2c {in_val[1][0]}: {xor_out}')

#####################################################
#                   PROBLEM XOR 2c                  #
#       bez użycia nadmiarowej instrukcji 'if'      #
#####################################################

# Założenie jest takie, że od instrukcji 'OR' odejmiemy 'AND' i wyjdzie 'XOR'

# Przygotujmy wektor na odpowiedzi dwóch perceptronów prostych i warstwy ukrytej
xor_proste = np.array([[0], [0]])
xor_ukryta = np.array([[0], [0]])

# Równania prostych Ax + By + C = 0
A1, B1, C1 = 2, 0, -1
A2, B2, C2 = 0, 2, -1

# Perceptron wejściowy 1
# Po przekształceniu x0 - x(y0) = 0 -> Ax0/A + By0/A = -C/A -> sprawdzanie lewo/prawo
xor_prosta_1 = np.array([[A1/A1, B1/A1]])
xor_b1 = -C1/A1

# Perceptron wejściowy 2
# Po przekształceniu y0 - y(x0) = 0 -> Ax0/B + By0/B = -C/B -> sprawdzanie góra/dół
xor_prosta_2 = np.array([[A2/B2, B2/B2]])
xor_b2 = -C2/B2

# Perceptron warstwy ukrytej 1
# Jego celem jest wykrywanie OR
xor_ukryta_param1 = np.array([[1, 1]])
xor_ukryta_b1 = 1  # Wykrywa albo góra, albo prawo

# Perceptron warstwy ukrytej 2
# Jego celem jest wykrywanie AND
xor_ukryta_param2 = np.array([[1, 1]])
xor_ukryta_b2 = 2  # Wykryrwa góra oraz prawo

# Perceptron wyjściowy
xor_out_param = np.array([[1, -1]])  # XOR jest kiedy jest OR, ale nie ma AND
xor_outb = 1

# Najpierw sprawdź, czy jest na prawo od pionowej i ponad poziomą prostą
xor_proste[0] = 1 if np.dot(xor_prosta_1, in_val) >= xor_b1 else 0  # Wykryte prawo
xor_proste[1] = 1 if np.dot(xor_prosta_2, in_val) >= xor_b2 else 0  # Wykryta góra

# Wykorzystaj te informacje, by określić OR i AND
xor_ukryta[0] = 1 if np.dot(xor_ukryta_param1, xor_proste) >= xor_ukryta_b1 else 0  # OR
xor_ukryta[1] = 1 if np.dot(xor_ukryta_param2, xor_proste) >= xor_ukryta_b2 else 0  # AND

# Sprawdź, czy jest OR, ale nie ma AND
xor_out = 1 if np.dot(xor_out_param, xor_ukryta) >= xor_outb else 0

print(f'{in_val[0][0]} XOR 2d {in_val[1][0]}: {xor_out}')

#####################################################
#                PROBLEM SZACHOWNICY                #
#####################################################

# 3
#   A | B | A
# 2---+---+---
#   B | A | B
# 1---+---+---
#   A | B | A
# 0   1   2   3

# Współrzędne punktu:
point = np.array([[1.5], [1.5]])

# Sieć będzie posiadać cztery perceptrony wejściowe, po jednym na prostą
# oraz dwa perceptrony warstwy ukrytej.

# Przygotujmy wektor na odpowiedzi czterech perceptronów prostych i dwóch warstwy ukrytej
proste = np.array([[0], [0], [0], [0]])
ukryta = np.array([[0], [0]])

# Równania prostych Ax + By + C = 0:

A_up, B_up, C_up = 0, 1, -2
prosta_up = np.array([[A_up/B_up, B_up/B_up]])
up_b = -C_up/B_up

#    |   |      ^
# ---+---+---   |   Górna prosta sprawdza górę
#    |   |
# ---+---+---
#    |   |

A_down, B_down, C_down = 0, 1, -1
prosta_down = -np.array([[A_down/B_down, B_down/B_down]])
down_b = C_down/B_down

#    |   |
# ---+---+---
#    |   |
# ---+---+---   |   Dolna prosta sprawdza dół - odwrócony znak
#    |   |      v

A_left, B_left, C_left = 1, 0, -1
prosta_left = -np.array([[A_left/A_left, B_left/A_left]])
left_b = C_left/A_left

#   <--              Lewa prosta sprawdza lewo - odwrócony znak
#    |   |
# ---+---+---
#    |   |
# ---+---+---
#    |   |

A_right, B_right, C_right = 1, 0, -2
prosta_right = np.array([[A_right/A_right, B_right/A_right]])
right_b = -C_right/A_right

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
ukryta_param = np.array([1, 1, 1, 1])
ukryta_b1 = 1
ukryta_b2 = 2

# Perceptron wyjścia wskazuje TRUE, gdy punkt należy do A, oraz FALSE, gdy punkt należy do B
out_param = np.array([1, -1])
out_b = 0

# Perceptrony warstwy wejściowej
proste[0] = 1 if np.dot(prosta_up, point) >= up_b else 0  # Wykryta góra
proste[1] = 1 if np.dot(prosta_down, point) >= down_b else 0  # Wykryty dół
proste[2] = 1 if np.dot(prosta_left, point) >= left_b else 0  # Wykryte lewo
proste[3] = 1 if np.dot(prosta_right, point) >= right_b else 0  # Wykryte prawo

# Perceptrony warstwy ukrytej
ukryta[0] = 1 if np.dot(ukryta_param, proste) >= ukryta_b2 else 0  # Wykryte 2 detekcje
ukryta[1] = 1 if np.dot(ukryta_param, proste) >= ukryta_b1 else 0  # Wykryta 1 detekcja

# Perceptron wyjścia
out = 1 if np.dot(out_param, ukryta) >= out_b else 0  # TRUE oznacza A, FALSE oznacza B

print(f'Punkt x0 = {point[0][0]}, y0 = {point[1][0]} należy do zbioru {"A" if out else "B"}')
