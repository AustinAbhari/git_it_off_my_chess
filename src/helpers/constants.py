# TODO: make all the direction into constants and then multiply them by the number of moves they can do in that direction
from types import SimpleNamespace

STARTING_ROWS_DICTIONARY = {
    'black_pawns': 6,
    'black_pieces': 7,
    'white_pawns': 1,
    'white_pieces': 0
}

STARTING_COLUMNS_DICTIONARY = {
    'rook': [0, 7],
    'knight': [1, 6],
    'bishop': [2, 5],
    'king': 3,
    'queen': 4
}

MOVES_DICTIONARY = {
    'up': [-1, 0],
    'down': [1, 0],
    'left': [0, -1],
    'right': [0, 1],
    'up_right': [-1, 1],
    'up_left': [-1, -1],
    'down_right': [1, 1],
    'down_left': [1, -1]
}

MOVES = SimpleNamespace(**MOVES_DICTIONARY)
STARTING_ROWS = SimpleNamespace(**STARTING_ROWS_DICTIONARY)
STARTING_COLUMNS = SimpleNamespace(**STARTING_COLUMNS_DICTIONARY)
