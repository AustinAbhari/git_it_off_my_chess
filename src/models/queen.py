from .piece import piece


class queen(piece):
    def __init__(self, starting_point, team_name='black'):
        self.starting_point = starting_point
        # special handling for 2, 0 as ONLY valid for the first move
        self.valid_moveset = [
            [float('inf'), 0], [0, float('inf')], [float('-inf'), 0], [0, float('-inf')], [float('inf'), float('inf')], [float('-inf'), float('-inf')], [float('inf'), float('-inf')], [float('-inf'), float('inf')]]
        self.team_name = team_name
        super(queen, self).__init__(starting_point=starting_point,
                                   valid_moveset=self.valid_moveset, team_name=team_name)
