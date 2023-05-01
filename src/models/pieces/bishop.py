from src.models.pieces.piece import piece
from src.helpers.constants import MOVES
from src.helpers.translate_moves import move_any_number_of_spaces_in_direction


class bishop(piece):
    def __init__(self, team_name='white'):
        self.team_name = team_name
        self.piece_abbreviation = '♝' if team_name == 'white' else '♗'
        self.valid_moveset = [
            [[row * x for row in MOVES.up_right] for x in range(1, 8)],
            [[row * x for row in MOVES.up_left] for x in range(1, 8)],
            [[row * x for row in MOVES.down_right] for x in range(1, 8)],
            [[row * x for row in MOVES.down_left] for x in range(1, 8)],
        ]
