from .piece import piece
from src.helpers.constants import MOVES
from src.helpers.translate_moves import move_any_number_of_spaces_in_direction


class queen(piece):
    def __init__(self, team_name='white'):

        self.valid_moveset = [
            list(map(move_any_number_of_spaces_in_direction, MOVES.up)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.down)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.left)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.right)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.up_right)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.up_left)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.down_right)),
            list(map(move_any_number_of_spaces_in_direction, MOVES.down_left)),
        ]
        print(self.valid_moveset)
        self.team_name = team_name
        super(queen, self).__init__(
            valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = '♕' if team_name == 'white' else '♛'
