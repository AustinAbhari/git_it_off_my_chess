import numpy as np


def valid_moves(move_set, current_position, piece, team_positions=[], opposition_positions=[]):
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

    for set in move_set:
        for move in set:
            print(list(move))
            # if you are at [0, 0] - and "move" is [1,0], this would be checking the postion at [1,0]
            # if you are at [1, 1] - and "move" is [2,0], this would be checking the postion at [3,1] - might not be a valid move but that's what numpy does
            possible_destination = np.add(current_position, move)

            # captures
            # if any(np.array_equal(x, possible_destination) for x in opposition_positions):
            if any(piece.can_capture(x, possible_destination) for x in opposition_positions):
                moves['captures'].append(possible_destination)
                break

            # if the array is greater than ceil or lower than floor break out of this set or hits a friendly
            if any(i > bounday_ceil for i in possible_destination) or any(i < boundary_floor for i in possible_destination) or any(np.array_equal(x, possible_destination) for x in team_positions):
                break

            moves['moves'].append(possible_destination)

    # pass in grid or somthing to get the collisions
    return moves
