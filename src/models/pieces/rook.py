from src.models.pieces.piece import piece
from src.helpers.constants import MOVES
from src.helpers.translate_moves import move_any_number_of_spaces_in_direction


class rook(piece):
    def __init__(self, team_name='white'):
        self.team_name = team_name
        self.piece_abbreviation = '♜' if team_name == 'white' else '♖'
        self.valid_moveset = [
            [[row * x for row in MOVES.up] for x in range(1, 8)],
            [[row * x for row in MOVES.down] for x in range(1, 8)],
            [[row * x for row in MOVES.left] for x in range(1, 8)],
            [[row * x for row in MOVES.right] for x in range(1, 8)],
        ]
        self.capture_direction = []
