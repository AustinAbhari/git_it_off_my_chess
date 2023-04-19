import numpy as np
import warnings


def valid_moves(move_set, current_position):
    if type(move_set) != list and type(move_set) != current_position:
        warnings.warn('bruh, move_set and current_position must be list')
    boundary_floor = 0
    bounday_ceil = 7
    moves = []

    for set in move_set:
        for move in set:
            m = np.add(current_position, move)
            if any(i > bounday_ceil for i in m) or any(i < boundary_floor for i in m):
                break
            moves.append(m)

    # pass in grid or somthing to get the collisions
    return moves
