from src.models.board import board
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

    def validate_and_move(self, from_grid_position, to_grid_position):
        enemy_pieces = self.board.alive_black_pieces if self.white_turn else self.board.alive_white_pieces
        friendly_pieces = self.board.alive_white_pieces if self.white_turn else self.board.alive_black_pieces

        if from_grid_position in enemy_pieces or not self.board.is_piece_in_grid(from_grid_position):
            # Throw expection or reason why fail
            return

        # Check for Capture first, also check for valid capture here
        if to_grid_position in enemy_pieces:
            self.board.capture_piece(
                from_grid_position, to_grid_position, friendly_pieces, enemy_pieces, self.white_turn)
        # Else just move the piece
        else:
            self.board.move_piece(from_grid_position,
                                  to_grid_position, friendly_pieces, self.white_turn)

        self.white_turn = not self.white_turn

    def find_valid_moves(self, grid_position):
        piece = self.board.grid[grid_position[0]][grid_position[1]].piece
        if piece == None:
            return []
        return valid_moves(piece.valid_moveset, grid_position, self.get_team_pieces(piece), self.get_opposition_pieces(piece))

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
