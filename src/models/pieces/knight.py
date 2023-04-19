from src.models.pieces.piece import piece


class knight(piece):
    # Current thoughts on this:
    # We should only care about starting position if it has a special move on that square
    # Which those constances would be put in the constances file asp
    # We should pass in the board class and get back legal moves
    def __init__(self, starting_point, team_name):
        # self.current_position = current_position
        self.starting_point = starting_point
        team_name = team_name
        self.valid_moveset = []
        super(knight, self).__init__(starting_point=starting_point,
                                   valid_moveset=self.valid_moveset, team_name=team_name)
        self.piece_abbreviation = 'Kn'
