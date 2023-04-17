from src.models.pieces.piece import piece
from src.helpers.constants import MOVES
from src.helpers.translate_moves import move_any_number_of_spaces_in_direction


class knight(piece):
    def __init__(self, team_name='white'):
        self.team_name = team_name
        self.piece_abbreviation = '♘' if team_name == 'white' else '♞'
