# Archiwum GitHub: https://github.com/Gierszu/SSN
from lab1_and import lab1_and
from lab1_or import lab1_or
from lab1_xor_2b import lab1_xor_2b
from lab1_xor_2c import lab1_xor_2c
from lab1_xor_2d import lab1_xor_2d
from lab1_chessboard import lab1_chessboard
import os
import json


# Opis działania funkcji znajduje się w odpowiednich plikach.

# Sprawdzenie dla wszystkich kombinacji;
# Funkcja od razu wypluwa dictionary z wagami i progamii printuje wyniki do konsoli
print(f'*----------------------*')
and_dict = [lab1_and(x, y) for x in range(2) for y in range(2)]
print(f'*----------------------*')
or_dict = [lab1_or(x, y) for x in range(2) for y in range(2)]
print(f'*----------------------*')
xor_2b_dict = [lab1_xor_2b(x, y) for x in range(2) for y in range(2)]
print(f'*----------------------*')
xor_2c_dict = [lab1_xor_2c(x, y) for x in range(2) for y in range(2)]
print(f'*----------------------*')
xor_2d_dict = [lab1_xor_2d(x, y) for x in range(2) for y in range(2)]
print(f'*----------------------*')
nums = [0.5, 1.5, 2.5]
chessboard_dict = [lab1_chessboard(x, y) for x in nums for y in nums]
print(f'*----------------------*')

# Konwersja do .json
networks = {
    'networks': {
        'and': and_dict[0],
        'or': or_dict[0],
        'xor_2b': xor_2b_dict[0],
        'xor_2c': xor_2c_dict[0],
        'xor_2d': xor_2d_dict[0],
        'chessboard': chessboard_dict[0]
    }
}

with open(os.path.join(os.getcwd(), 'lab1_network_data.json'), 'w') as file:
    json.dump(networks, file, indent=4, sort_keys=False)
