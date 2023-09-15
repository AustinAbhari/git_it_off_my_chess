import pytest
from src.util.valid_moves import valid_moves
from src.helpers.constants import MOVES


def test_valid_moves_single_move():
    move_set = [[MOVES.right]]
    current_position = [2, 2]
    moves = valid_moves(move_set, current_position)
    expected_output = [[2, 3]]
    valid_move_set = moves['moves']

    assert len(valid_move_set) == 1
    assert (valid_move_set[0] == expected_output[0]).all()


def test_valid_moves_in_four_directions():
    move_set = [[MOVES.right], [MOVES.left], [MOVES.up], [MOVES.down]]
    current_position = [4, 4]
    moves = valid_moves(move_set, current_position)
    expected_output = [[4, 5], [4, 3], [3, 4], [5, 4]]
    valid_move_set = moves['moves']

    assert len(valid_move_set) == 4
    for x in range(len(valid_move_set)):
        assert (valid_move_set[x] == expected_output[x]).all()


def test_valid_moves_boundaries():
    move_set = [[MOVES.up], [MOVES.left]]
    current_position = [0, 0]
    valid_move_set = valid_moves(move_set, current_position)

    assert not valid_move_set['moves']


def test_find_captures():
    move_set = [[MOVES.down], [MOVES.right]]
    current_position = [0, 0]
    enemy_piece = [[1, 0]]
    moves = valid_moves(move_set, current_position, [], enemy_piece)
    valid_captures = moves['captures']
    valid_move_set = moves['moves']

    assert len(valid_move_set) == 1
    assert (valid_captures[0] == enemy_piece[0]).all()
    assert (valid_move_set[0] == [0, 1]).all()


def test_handle_collisions():
    move_set = [[[row * x for row in MOVES.down] for x in range(1, 8)]]
    current_position = [0, 0]
    friendly_piece = [[4, 0]]
    moves = valid_moves(move_set, current_position, friendly_piece)
    valid_move_set = moves['moves']

    assert len(valid_move_set) == 3


def test_capture_direction():
    move_set = []
    current_position = [0, 0]
    enemy_piece = [[1, 1]]
    capture_direction = [[1, -1], [1, 1]]
    moves = valid_moves(move_set, current_position, [],
                        enemy_piece, capture_direction)
    valid_captures = moves['captures']
    assert (valid_captures[0] == [1,1]).all()
