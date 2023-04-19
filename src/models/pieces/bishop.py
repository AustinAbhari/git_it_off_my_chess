from src.models.pieces.piece import piece


class bishop(piece):
    def __init__(self, starting_point, team_name):
        self.starting_point = starting_point
        self.team_name = team_name
        self.valid_moveset = []
        super(bishop, self).__init__(starting_point=starting_point,
                                     valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = 'B'
