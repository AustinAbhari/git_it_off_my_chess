import numpy as np


def valid_moves(move_set, current_position, team_positions=[], opposition_positions=[], capture_direction=[]):
    """
    Get the valid moves on the board

    Attributes:
        move_set (list(list(list(int, int)))): moves where the piece can go
        current_position  (list(int, int)): The imaginary part of complex number.
    """
    boundary_floor = 0
    bounday_ceil = 7
    moves = {
        'captures': [],
        'moves': []
    }

    if type(move_set) != list and type(move_set) != current_position:
        raise Exception('Bruh, move_set and current_position must be list')

    for capture in capture_direction:
        potential_capture = np.add(current_position, capture)
        if any(np.array_equal(x, potential_capture) for x in opposition_positions):
            moves['captures'].append(potential_capture)

    for set in move_set:
        for move in set:
            m = np.add(current_position, move)

            # Don't go through opposition team if capture direction
            if (any(np.array_equal(x, m) for x in opposition_positions) and capture_direction):
                break

            # Captures
            if (any(np.array_equal(x, m) for x in opposition_positions) and (not capture_direction)):
                moves['captures'].append(m)
                break

            # if the array is greater than ceil or lower than floor break out of this set or hits a friendly
            if any(i > bounday_ceil for i in m) or any(i < boundary_floor for i in m) or any(np.array_equal(x, m) for x in team_positions):
                break

            moves['moves'].append(m)

    # pass in grid or somthing to get the collisions
    return moves
