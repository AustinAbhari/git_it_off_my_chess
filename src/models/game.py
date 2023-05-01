from src.models.board import board


class Game():
    # turn
    # show valid moves
    def __init__(self, white_turn=True):
        # change turn to white or black, prolly move this is a game class
        # catalog in move order
        # re-call valid moves on each peice in the array
        self.board = board()
        self.white_turn = white_turn
        self.move_log = []

    def new_game(self):
        self.board.setup_board()

    # check valid move
    # update grid
    # next_turn
    def validate_and_move(self, from_grid_position, to_grid_position):
        # check if peice moving is on the correct time to the turn
        # need to clean this up, might not actually need to check alive pieces here
        # since the board handles if its there just need to update it
        if self.white_turn:
            if from_grid_position in self.board.alive_white_pieces:
                self.move_and_flip(from_grid_position,
                                   to_grid_position)
            else:
                print('its whites turn')
        elif not self.white_turn:
            if from_grid_position in self.board.alive_black_pieces:
                self.move_and_flip(from_grid_position,
                                   to_grid_position)
            else:
                print('its blacks turn')
        else:
            print('invalid move')

    def move_and_flip(self, from_grid_position, to_grid_position):
        self.board.move_piece(from_grid_position, to_grid_position)
        self.white_turn = not self.white_turn

    def print_board(self):
        print(self.grid)
