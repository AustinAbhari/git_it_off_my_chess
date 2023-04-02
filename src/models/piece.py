class piece:
    def __init__(self, starting_point, valid_moveset, team_name = 'black'):
        self.starting_point = starting_point
        self.valid_moveset = valid_moveset
        self.team_name = team_name
        print(__class__.__name__)
