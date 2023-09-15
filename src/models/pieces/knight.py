from src.models.pieces.piece import piece
from src.helpers.constants import KNIGHT_MOVES
import numpy as np


class knight(piece):
    def __init__(self, team_name='white'):
        self.team_name = team_name
        self.piece_abbreviation = '♞' if team_name == 'white' else '♘'
        self.valid_moveset = [
            [KNIGHT_MOVES.up_up_right],
            [KNIGHT_MOVES.up_up_left],
            [KNIGHT_MOVES.down_down_right],
            [KNIGHT_MOVES.down_down_left],
            [KNIGHT_MOVES.right_right_up],
            [KNIGHT_MOVES.right_right_down],
            [KNIGHT_MOVES.left_left_up],
            [KNIGHT_MOVES.left_left_down]
        ]
        self.capture_direction = []
