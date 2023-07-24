import pytest
import pdb
from src.models.pieces.pawn import pawn
from src.helpers.constants import MOVES


@pytest.mark.black_team
def test_has_correct_valid_moveset():
    assert pawn(team_name="black").valid_moveset == [[[-1, 0], [-2, 0]]]


def test_has_correct_valid_moveset_at_turn_2():
    my_pawn = pawn(team_name="black")
    my_pawn.end_turn()
    assert my_pawn.valid_moveset == [[[-1, 0]]]


@pytest.mark.white_team
def test_has_correct_valid_moveset_white():
    my_pawn = pawn()
    assert my_pawn.valid_moveset == [[[1, 0], [2, 0]]]


def test_has_correct_valid_moveset_at_turn_2_white():
    my_pawn = pawn()
    my_pawn.end_turn()
    assert my_pawn.has_moved == True
    assert my_pawn.valid_moveset == [[[1, 0]]]
