from src.models.board import board


class game():
    # turn
    # show valid moves
    def __init__(self, white_turn=True):
        # change turn to white or black, prolly move this is a game class
        # catalog in move order
        # re-call valid moves on each peice in the array
        self.board = board()
        self.white_turn = white_turn

    def new_game(self):
        self.board.setup_board()

    def piece_move(self, from_grid_position, to_grid_position):
        self.white_turn = not self.white_turn
        # check valid move
        # update grid
        # next_turn
        return None

    def print_board(self):
        print(self.grid)
