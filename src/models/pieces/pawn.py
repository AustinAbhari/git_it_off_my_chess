from .piece import piece
from src.helpers.constants import MOVES
from src.helpers.constants import PAWN_MOVES
import numpy as np

class pawn(piece):
    def __init__(self, team_name='white'):
        # self.valid_moveset = [[-1, 0], [-2, 0]] #
        # special handling for 2, 0 as ONLY valid for the first move
        self.team_name = team_name
        self.valid_moveset = [[MOVES.down, PAWN_MOVES.down_down]
                              ] if team_name == 'white' else [[MOVES.up, PAWN_MOVES.up_up]]
        self.has_moved = False
        super(pawn, self).__init__(team_name=team_name)
        self.piece_abbreviation = '♟︎' if team_name == 'white' else '♙'

    def end_turn(self):
        if self.has_moved == False:
            self.valid_moveset[0].pop() 
            self.has_moved = True
        
        return super().end_turn()

    def can_capture(self, enemy_position, possible_capture_position):
        return not np.array_equal(enemy_position, possible_capture_position)

    # convert the moveset based on team/starting position
    # example: "up" for the black team is [-1, 0] - but if you're the white team
    # "up" would be [1, 0] - so we just multiply the "y-axis" move move by -1
    def convert_moveset_based_on_team(self, moveset):
        if self.team_name == 'white':
            converted_moveset = []
            for move in moveset[0]:
                print(move)
                move[0] = move[0] * -1
                converted_moveset.append(move)
            print(converted_moveset)
            return converted_moveset
        else:
            return self.valid_moveset
