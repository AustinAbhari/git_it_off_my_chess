from src.models.board import board
from src.helpers.double_array_indexer import double_array_indexer
from src.util.valid_moves import valid_moves


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
        # need to clean this up
        if self.white_turn:
            if from_grid_position in self.board.alive_white_pieces:
                if double_array_indexer(self.board.grid, to_grid_position).piece != None:
                    self.board.capture_piece(
                        from_grid_position, to_grid_position)
                    alive_pieces = self.update_captured_piece()
                    self.board.alive_white_pieces = alive_pieces[0]
                    self.board.alive_black_pieces = alive_pieces[1]
                else:
                    self.move_and_flip(from_grid_position,
                                       to_grid_position)
                    self.board.alive_white_pieces = self.update_pieces(
                        from_grid_position, to_grid_position, self.board.alive_white_pieces)
            else:
                print('its whites turn')
        elif not self.white_turn:
            print("black turn")
            if from_grid_position in self.board.alive_black_pieces:
                self.move_and_flip(from_grid_position,
                                   to_grid_position)
                self.board.alive_black_pieces = self.update_pieces(
                    from_grid_position, to_grid_position, self.board.alive_black_pieces)
            else:
                print('its blacks turn')
        else:
            print('invalid move')

    def find_valid_moves(self, grid_position):
        piece = double_array_indexer(self.board.grid, grid_position).piece
        if piece == None:
            return []
        return valid_moves(piece.valid_moveset, grid_position, self.get_team_pieces(piece), self.get_opposition_pieces(piece))

    def move_and_flip(self, from_grid_position, to_grid_position):
        self.board.move_piece(from_grid_position, to_grid_position)
        self.white_turn = not self.white_turn

    def update_captured_piece(self, from_grid_position, to_grid_position, from_alive_pieces, to_alive_pieces):
        from_alive_pieces.append(to_grid_position)
        from_alive_pieces.remove(from_grid_position)
        to_alive_pieces.remove(to_grid_position)
        return [from_alive_pieces, to_alive_pieces]

    def update_pieces(self, from_grid_position, to_grid_position, alive_pieces):
        alive_pieces.append(to_grid_position)
        alive_pieces.remove(from_grid_position)
        return alive_pieces

    def get_team_pieces(self, piece):
        return self.board.alive_white_pieces if piece.team_name == 'white' else self.board.alive_black_pieces

    def get_opposition_pieces(self, piece):
        return self.board.alive_white_pieces if not piece.team_name == 'white' else self.board.alive_black_pieces

    def print_board(self):
        print(self.grid)
