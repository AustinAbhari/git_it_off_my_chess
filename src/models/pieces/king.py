from .piece import piece
from src.helpers.constants import MOVES


class king(piece):
    def __init__(self, team_name='white'):
        # special handling for 2, 0 as ONLY valid for the first move
        self.valid_moveset = [MOVES.up, MOVES.down, MOVES.left, MOVES.right,
                              MOVES.up_right, MOVES.up_left, MOVES.down_left, MOVES.down_right]
        self.team_name = team_name
        super(king, self).__init__(
            valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = '♔' if team_name == 'white' else '♚'
