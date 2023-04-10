from src.models.pieces.piece import piece


class bishop(piece):
    def __init__(self, current_position, team_name):
        self.current_position = current_position
        self.team_name = team_name
        self.piece_abbreviation = 'B'
