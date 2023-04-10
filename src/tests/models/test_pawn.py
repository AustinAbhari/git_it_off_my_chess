import pytest
import pdb
from src.models.peices.pawn import pawn
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    assert pawn(starting_point='fuck you').valid_moveset == [[-1, 0], [-2, 0]]


def test_has_correct_valid_moveset_at_turn_2():
    my_pawn = pawn(starting_point='fuck you')
    my_pawn.end_turn()
    assert my_pawn.valid_moveset == [[-1, 0]]


def test_has_correct_black_team_piece_representation():
    assert pawn(starting_point='fuck you').team_piece_representation() == 'bP'


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_pawn = pawn(team_name='white', starting_point='fuck you')
    assert my_pawn.valid_moveset == [[1, 0], [2, 0]]


def test_has_correct_valid_moveset_at_turn_2_white():
    my_pawn = pawn(team_name='white', starting_point='fuck you')
    my_pawn.end_turn()
    assert my_pawn.turn_number == 1
    assert my_pawn.valid_moveset == [[1, 0]]


def test_has_correct_white_team_piece_representation():
    assert pawn(team_name='white',
                starting_point='fuck you').team_piece_representation() == 'wP'
