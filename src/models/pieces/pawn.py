from .piece import piece
from src.helpers.constants import MOVES


class pawn(piece):
    def __init__(self, team_name='white'):
        # self.valid_moveset = [[-1, 0], [-2, 0]] #
        # special handling for 2, 0 as ONLY valid for the first move
        self.team_name = team_name
        self.valid_moveset = [MOVES.up.copy(), list(
            map(lambda x: x * 2, MOVES.up))]
        self.valid_moveset = self.convert_moveset_based_on_team(
            self.valid_moveset)
        super(pawn, self).__init__(
            valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = '♙' if team_name == 'white' else '♟︎'

    def end_turn(self):
        self.valid_moveset.pop() if self.turn_number == 0 else False
        return super().end_turn()

    # convert the moveset based on team/starting position
    # example: "up" for the black team is [-1, 0] - but if you're the white team
    # "up" would be [1, 0] - so we just multiply the "y-axis" move move by -1
    def convert_moveset_based_on_team(self, moveset):
        if self.team_name == 'white':
            converted_moveset = []
            for move in moveset:
                move[0] = move[0] * -1
                converted_moveset.append(move)
            return converted_moveset
        else:
            return self.valid_moveset
