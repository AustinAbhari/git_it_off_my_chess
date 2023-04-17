import numpy as np


def valid_moves(move_set, current_position):
    boundary_floor = -1
    bounday_ceil = 8
    moves = []

    for set in move_set:
        for move in set:
            m = np.add(current_position, move)
            if any(i > 7 for i in m) or any(i < 0 for i in m):
                break
            moves.append(m)

    # pass in grid or somthing to get the collisions
    return moves
