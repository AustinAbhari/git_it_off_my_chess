import pytest
import pdb
from src.models.pieces.king import king
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    my_king = king()
    assert all(elem in my_king.valid_moveset for elem in [[1, 0], [0, 1], [-1, 0],
                                                          [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]])


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_king = king(team_name='white')
    assert all(elem in my_king.valid_moveset for elem in [[1, 0], [0, 1], [-1, 0],
                                                          [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]])
