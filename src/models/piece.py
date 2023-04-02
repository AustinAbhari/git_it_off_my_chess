class piece:
    def __init__(self, starting_point, valid_moveset, team_name = 'black'):
        self.starting_point = starting_point
        # TODO: convert valid_moveset into simple namespace
        # so we can build a SimpleNamespace (dot notation dictionary, basically)
        # or a normal dictionary of the valid moveset - it will be easier to work with
        self.valid_moveset = valid_moveset 
        self.team_name = team_name
        print(__class__.__name__)

    # add direction as an argument once we have this converted as valid_movesets
    def move_x_spaces_in_direction(self, x):
        print("this is x %d: " % x )
        return map(lambda y: y * x, self.valid_moveset[0])