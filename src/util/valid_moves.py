import numpy as np


def valid_moves(move_set, current_position):
    """
    Get the valid moves on the board

    Attributes:
        move_set (list(list(list(int, int)))): moves where the piece can go
        current_position  (list(int, int)): The imaginary part of complex number.
    """
    boundary_floor = 0
    bounday_ceil = 7
    moves = []

    if type(move_set) != list and type(move_set) != current_position:
        raise Exception('Bruh, move_set and current_position must be list')

    for set in move_set:
        for move in set:
            m = np.add(current_position, move)
            # if the array is greater than ceil or lower than floor break out of this set
            if any(i > bounday_ceil for i in m) or any(i < boundary_floor for i in m):
                break
            moves.append(m)

    # pass in grid or somthing to get the collisions
    return moves
