import pytest
from src.util.valid_moves import valid_moves
import numpy as np
from src.helpers.constants import MOVES


def test_valid_moves_single_move():
    move_set = [[1, 0], [0, 1], [-1, 0]]
    current_position = [2, 2]
    print(valid_moves(move_set, current_position))


# def test_move_set():
#     moves = [
#         [[row * x for row in MOVES.up_right] for x in range(1, 7)],
#         [[row * x for row in MOVES.up_left] for x in range(1, 7)],
#         [[row * x for row in MOVES.down_right] for x in range(1, 7)],
#         [[row * x for row in MOVES.down_left] for x in range(1, 7)],
#     ]

#     print(valid_moves(moves, [4, 4]))
