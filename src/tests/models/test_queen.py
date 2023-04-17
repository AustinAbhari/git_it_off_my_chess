import pytest
import pdb
from src.models.pieces.queen import queen
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    assert queen().valid_moveset == [[float('-inf'), 0], [float('inf'), 0], [0, float('-inf')], [0, float(
        'inf')], [float('-inf'), float('inf')], [float('-inf'), float('-inf')], [float('inf'), float('inf')], [float('inf'), float('-inf')]]


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_queen = queen(team_name='white', )
    assert my_queen.valid_moveset == [[float('-inf'), 0], [float('inf'), 0], [0, float('-inf')], [0, float('inf')], [float(
        '-inf'), float('inf')], [float('-inf'), float('-inf')], [float('inf'), float('inf')], [float('inf'), float('-inf')]]
