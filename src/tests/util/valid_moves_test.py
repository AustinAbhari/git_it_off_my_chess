import pytest
from src.util.valid_moves import valid_moves
from src.helpers.constants import MOVES


def test_valid_moves_single_move():
    move_set = [[MOVES.right]]
    current_position = [2, 2]
    valid_move_set = valid_moves(move_set, current_position)
    expected_output = [[2, 3]]

    assert len(valid_move_set) == 1
    assert (valid_move_set[0] == expected_output[0]).all()


def test_valid_moves_in_four_directions():
    move_set = [[MOVES.right], [MOVES.left], [MOVES.up], [MOVES.down]]
    current_position = [4, 4]
    valid_move_set = valid_moves(move_set, current_position)
    expected_output = [[4, 5], [4, 3], [3, 4], [5, 4]]

    assert len(valid_move_set) == 4
    for x in range(len(valid_move_set)):
        assert (valid_move_set[x] == expected_output[x]).all()


def test_valid_moves_boundaries():
    move_set = [[MOVES.up], [MOVES.left]]
    current_position = [0, 0]
    valid_move_set = valid_moves(move_set, current_position)

    assert not valid_move_set
