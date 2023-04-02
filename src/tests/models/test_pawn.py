from unittest import TestCase
from src.models.pawn import pawn
from src.models.constants import MOVES

def test_has_correct_valid_moveset():
    assert pawn(starting_point='fuck you').valid_moveset == [[-1, 0], [-2,0]]

def test_has_correct_valid_moveset_at_turn_2():
    my_pawn = pawn(starting_point='fuck you')
    my_pawn.end_turn()
    assert my_pawn.valid_moveset == [[-1, 0]]
