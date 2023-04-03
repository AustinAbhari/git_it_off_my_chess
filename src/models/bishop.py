from src.models.piece import piece


class bishop(piece):
    def __init__(self, current_position, team_name):
        self.current_position = current_position
        team_name = team_name
