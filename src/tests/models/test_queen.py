import pytest
import pdb
from src.models.queen import queen
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    assert queen(starting_point='fuck you').valid_moveset == [[float('-inf'), 0], [float('inf'), 0], [0, float('-inf')], [0, float('inf')], [float('-inf'), float('inf')], [float('-inf'), float('-inf')], [float('inf'), float('inf')], [float('inf'), float('-inf')]]

def test_has_correct_black_team_piece_representation():
    assert queen(starting_point='fuck you').team_piece_representation() == 'bQ'


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_queen = queen(team_name='white', starting_point='fuck you')
    assert my_queen.valid_moveset == [[float('-inf'), 0], [float('inf'), 0], [0, float('-inf')], [0, float('inf')], [float('-inf'), float('inf')], [float('-inf'), float('-inf')], [float('inf'), float('inf')], [float('inf'), float('-inf')]]

def test_has_correct_white_team_piece_representation():
    assert queen(team_name='white',
                starting_point='fuck you').team_piece_representation() == 'wQ'
