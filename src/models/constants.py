# TODO: make all the direction into constants and then multiply them by the number of moves they can do in that direction
from types import SimpleNamespace

MOVES_DICTIONARY = {
    'up': [-1,0],
    'down': [1,0],
    'left': [0, -1],
    'right': [0, 1],
    'up_right': [-1, 1],
    'up_left': [-1, -1],
    'down_right': [1, 1],
    'down_left': [1, -1]
}

MOVES = SimpleNamespace(**MOVES_DICTIONARY)