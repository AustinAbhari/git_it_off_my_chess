import pdb


class piece:
    def __init__(self, valid_moveset, team_name='white'):
        # TODO: convert valid_moveset into simple namespace
        # so we can build a SimpleNamespace (dot notation dictionary, basically)
        # or a normal dictionary of the valid moveset - it will be easier to work with
        self.team_name = team_name
        self.valid_moveset = valid_moveset
        self.turn_number = 0
        self.piece_abbreviation = None
        self.has_moved = False
        self.capture_direction = []

    # add direction as an argument once we have this converted as valid_movesets
    def move_x_spaces_in_direction(self, x):
        print("this is x %d: " % x)
        return map(lambda y: y * x, self.valid_moveset[0])

    def moved(self):
        self.has_moved = True

    def get_valid_moveset(self):
        print(self.valid_moveset)
        return self.valid_moveset
