from .piece import piece
from .constants import MOVES
class pawn(piece):
    def __init__(self, starting_point, team_name = 'black'):
        self.starting_point = starting_point
        # self.valid_moveset = [[-1, 0], [-2, 0]] # 
        self.valid_moveset = [MOVES.up.copy(), list(map(lambda x: x * 2, MOVES.up))] # special handling for 2, 0 as ONLY valid for the first move
        self.team_name = team_name
        super(pawn, self).__init__(starting_point=starting_point, valid_moveset=self.valid_moveset, team_name=team_name)
    
    def end_turn(self):
        self.valid_moveset.pop() if self.turn_number == 0 else False
        return super().end_turn()