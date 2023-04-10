import pytest
import pdb
from src.models.pieces.king import king
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    my_king = king(starting_point='fuck you')
    assert all(elem in my_king.valid_moveset for elem in [[1, 0], [0, 1], [-1, 0],
                                                                                  [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]])


def test_has_correct_black_team_piece_representation():
    assert king(starting_point='fuck you').team_piece_representation() == 'bK'


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_king = king(team_name='white', starting_point='fuck you')
    assert all(elem in my_king.valid_moveset for elem in [[1, 0], [0, 1], [-1, 0],
                                                                                  [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]])


def test_has_correct_white_team_piece_representation():
    assert king(team_name='white',
                 starting_point='fuck you').team_piece_representation() == 'wK'
