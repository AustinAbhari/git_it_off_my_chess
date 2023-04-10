from .piece import piece


class king(piece):
    def __init__(self, starting_point, team_name='black'):
        self.starting_point = starting_point
        # special handling for 2, 0 as ONLY valid for the first move
        self.valid_moveset = [[1, 0], [0, 1], [-1, 0],
                              [0, -1], [1, 1], [-1, -1], [-1, 1], [1, -1]]
        self.team_name = team_name
        super(king, self).__init__(starting_point=starting_point,
                                    valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = 'K'
