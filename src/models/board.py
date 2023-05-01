from src.models.square import square
from src.models.pieces.bishop import bishop
from src.models.pieces.pawn import pawn
from src.models.pieces.knight import knight
from src.models.pieces.rook import rook
from src.models.pieces.queen import queen
from src.models.pieces.king import king
from src.helpers.constants import STARTING_COLUMNS, STARTING_ROWS
from src.util.valid_moves import valid_moves
from src.helpers.double_array_indexer import double_array_indexer

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
        return self.alive_black_pieces

    def set_alive_black_pieces(self, x):
        self.alive_black_pieces = x

    alive_black_pieces = property(
        get_alive_black_pieces, set_alive_black_pieces)

    def move_piece(self, from_grid_position, to_grid_position):
        to_square = double_array_indexer(self.grid, to_grid_position)
        from_square = double_array_indexer(self.grid, from_grid_position)

        # need more validation here for: collisions, captures, valid moves
        if (to_square.piece == None and from_square.piece != None):
            to_square.piece = from_square.piece
            from_square.piece = None

    def find_valid_moves(self, grid_position):
        piece = double_array_indexer(self.grid, grid_position).piece
        if piece == None:
            return []
        return valid_moves(piece.valid_moveset, grid_position)

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
                    i+j) % 2 == 1 else 'lightgreen'

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
