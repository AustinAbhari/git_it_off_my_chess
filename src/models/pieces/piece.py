import pdb
import numpy as np

class piece:
    def __init__(self, team_name='white'):
        # TODO: convert valid_moveset into simple namespace
        # so we can build a SimpleNamespace (dot notation dictionary, basically)
        # or a normal dictionary of the valid moveset - it will be easier to work with
        self.team_name = team_name
        self.turn_number = 0
        self.piece_abbreviation = None

    # add direction as an argument once we have this converted as valid_movesets
    def move_x_spaces_in_direction(self, x):
        print("this is x %d: " % x)
        return map(lambda y: y * x, self.valid_moveset[0])

    def end_turn(self):
        return None
    
    # most pieces can capture an opposite team's piece by jumping on top of it like a fucking goomba
    # EXCEPT the pawn.
    def can_capture(self, enemy_position, possible_capture_position):
        return np.array_equal(enemy_position, possible_capture_position)

    def get_valid_moveset(self):
        print(self.valid_moveset)
        return self.valid_moveset
