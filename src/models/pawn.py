from .piece import piece
class pawn(piece):
    def __init__(self, starting_point, team_name = 'black'):
        self.starting_point = starting_point
        self.valid_moveset = [[1,0], [2, 0]] # special handling for 2, 0 as ONLY valid for the first move
        self.team_name = team_name
        super(pawn, self).__init__(starting_point=starting_point, valid_moveset=self.valid_moveset, team_name=team_name)
