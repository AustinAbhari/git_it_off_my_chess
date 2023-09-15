from src.models.square import square
from src.models.pieces.bishop import bishop
from src.models.pieces.pawn import pawn
from src.models.pieces.knight import knight
from src.models.pieces.rook import rook
from src.models.pieces.queen import queen
from src.models.pieces.king import king
from src.helpers.constants import STARTING_COLUMNS, STARTING_ROWS
from src.util.valid_moves import valid_moves

rows, cols = (8, 8)


class board:
    def __init__(self):
        self.grid = [[square() for i in range(cols)] for j in range(rows)]
        self._alive_white_pieces = []
        self._alive_black_pieces = []

    def get_grid(self):
        return self.grid

    def get_alive_white_pieces(self):
        return self._alive_white_pieces

    def set_alive_white_pieces(self, x):
        self._alive_white_pieces = x

    alive_white_pieces = property(
        get_alive_white_pieces, set_alive_white_pieces)

    def get_alive_black_pieces(self):
        return self._alive_black_pieces

    def set_alive_black_pieces(self, x):
        self._alive_black_pieces = x

    alive_black_pieces = property(
        get_alive_black_pieces, set_alive_black_pieces)

    def is_piece_in_grid(self, position):
        return self.grid[position[0]][position[1]].piece is not None

    def capture_piece(self, from_grid_position, to_grid_position, from_alive_pieces, to_alive_pieces, white_turn):
        piece = self.grid[from_grid_position[0]][from_grid_position[1]].piece
        if piece == None:
            return
        self.grid[from_grid_position[0]][from_grid_position[1]].piece = None
        self.grid[to_grid_position[0]][to_grid_position[1]].piece = piece

        # update alive piece matrix
        from_alive_pieces.append(to_grid_position)
        from_alive_pieces.remove(from_grid_position)
        to_alive_pieces.remove(to_grid_position)

        self.set_alive_black_pieces(
            to_alive_pieces if white_turn else from_alive_pieces)
        self.set_alive_white_pieces(
            to_alive_pieces if not white_turn else from_alive_pieces)

    def move_piece(self, from_grid_position, to_grid_position, friendly_pieces, white_turn):
        to_square = self.grid[to_grid_position[0]][to_grid_position[1]]
        from_square = self.grid[from_grid_position[0]][from_grid_position[1]]

        to_square.piece = from_square.piece
        to_square.piece.moved()
        from_square.piece = None

        friendly_pieces.remove(from_grid_position)
        friendly_pieces.append(to_grid_position)

        self.set_alive_white_pieces(
            friendly_pieces) if white_turn else self.set_alive_black_pieces(friendly_pieces)

    def display_valid_moves(self, moves):
        for move in moves:
            self.grid[move[0]][move[1]].color = 'yellow'

    def setup_board(self):
        self.checker_board()
        self.set_pawns()
        self.set_knights()
        self.set_rooks()
        self.set_bishops()
        self.set_yas_queens()
        self.set_short_kings()

    def checker_board(self):
        for i in range(rows):
            for j in range(cols):
                self.grid[i][j].color = 'black' if (
                    i+j) % 2 == 1 else 'MistyRose'

    def set_pawns(self):
        for i in range(0, cols):
            self.grid[STARTING_ROWS.white_pawns][i].piece = pawn(
                team_name='white')
            self.grid[STARTING_ROWS.black_pawns][i].piece = pawn(
                team_name='black')
            self._alive_white_pieces.append([STARTING_ROWS.white_pawns, i])
            self._alive_black_pieces.append([STARTING_ROWS.black_pawns, i])

    def set_knights(self):
        for x in STARTING_COLUMNS.knight:
            self.grid[STARTING_ROWS.white_pieces][x].piece = knight(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = knight(
                team_name='black')
            self._alive_white_pieces.append([STARTING_ROWS.white_pieces, x])
            self._alive_black_pieces.append([STARTING_ROWS.black_pieces, x])

    def set_rooks(self):
        for x in STARTING_COLUMNS.rook:
            self.grid[STARTING_ROWS.white_pieces][x].piece = rook(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = rook(
                team_name='black')
            self._alive_white_pieces.append([STARTING_ROWS.white_pieces, x])
            self._alive_black_pieces.append([STARTING_ROWS.black_pieces, x])

    def set_bishops(self):
        for x in STARTING_COLUMNS.bishop:
            self.grid[STARTING_ROWS.white_pieces][x].piece = bishop(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = bishop(
                team_name='black')
            self._alive_white_pieces.append([STARTING_ROWS.white_pieces, x])
            self._alive_black_pieces.append([STARTING_ROWS.black_pieces, x])

    def set_yas_queens(self):
        self.grid[STARTING_ROWS.white_pieces][STARTING_COLUMNS.queen].piece = queen(
            team_name='white')
        self.grid[STARTING_ROWS.black_pieces][STARTING_COLUMNS.queen].piece = queen(
            team_name='black')
        self._alive_white_pieces.append(
            [STARTING_ROWS.white_pieces, STARTING_COLUMNS.queen])
        self._alive_black_pieces.append(
            [STARTING_ROWS.black_pieces, STARTING_COLUMNS.queen])

    def set_short_kings(self):
        self.grid[STARTING_ROWS.white_pieces][STARTING_COLUMNS.king].piece = king(
            team_name='white')
        self.grid[STARTING_ROWS.black_pieces][STARTING_COLUMNS.king].piece = king(
            team_name='black')
        self._alive_white_pieces.append(
            [STARTING_ROWS.white_pieces, STARTING_COLUMNS.king])
        self._alive_black_pieces.append(
            [STARTING_ROWS.black_pieces, STARTING_COLUMNS.king])
