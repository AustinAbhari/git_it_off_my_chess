from src.models.pieces.piece import piece


class knight(piece):
    # Current thoughts on this:
    # We should only care about starting position if it has a special move on that square
    # Which those constances would be put in the constances file asp
    # We should pass in the board class and get back legal moves
    def __init__(self, current_position, team_name):
        self.current_position = current_position
        team_name = team_name
        self.piece_abbreviation = 'Kn'
