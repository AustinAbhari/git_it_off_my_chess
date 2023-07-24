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

PAWN_MOVES_DICTIONARY = {
    'up_up': [-2, 0],
    'down_down': [2, 0],
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

KNIGHT_MOVES_DICTIONARY = {
    'up_up_right': [-2, 1],
    'up_up_left': [-2, -1],
    'down_down_right': [2, -1],
    'down_down_left': [2, 1],
    'right_right_up': [-1, 2],
    'right_right_down': [1, 2],
    'left_left_up': [-1, -2],
    'left_left_down': [1, -2]
}


MOVES = SimpleNamespace(**MOVES_DICTIONARY)
KNIGHT_MOVES = SimpleNamespace(**KNIGHT_MOVES_DICTIONARY)
STARTING_ROWS = SimpleNamespace(**STARTING_ROWS_DICTIONARY)
STARTING_COLUMNS = SimpleNamespace(**STARTING_COLUMNS_DICTIONARY)
PAWN_MOVES = SimpleNamespace(**PAWN_MOVES_DICTIONARY)
