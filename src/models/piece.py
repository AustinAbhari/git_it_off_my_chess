import pdb
class piece:
    def __init__(self, starting_point, valid_moveset, team_name = 'black'):
        self.starting_point = starting_point
        # TODO: convert valid_moveset into simple namespace
        # so we can build a SimpleNamespace (dot notation dictionary, basically)
        # or a normal dictionary of the valid moveset - it will be easier to work with
        self.team_name = team_name
        self.valid_moveset = self.convert_moveset_based_on_team(valid_moveset)
        self.turn_number = 0
        print(__class__.__name__)

    # add direction as an argument once we have this converted as valid_movesets
    def move_x_spaces_in_direction(self, x):
        print("this is x %d: " % x )
        return map(lambda y: y * x, self.valid_moveset[0])
    
    def end_turn(self):
        self.turn_number += 1
    
    # convert the moveset based on team/starting position
    # example: "up" for the black team is [-1, 0] - but if you're the white team
    # "up" would be [1, 0] - so we just multiply the "y-axis" move move by -1
    def convert_moveset_based_on_team(self, moveset):
        if self.team_name == 'white':
            converted_moveset = []
            for move in moveset:
                move[0] = move[0] * -1
                converted_moveset.append(move)
            return converted_moveset
        else:
            return self.valid_moveset
