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

    def get_grid(self):
        return self.grid

    def move_piece(self, piece, grid_position):
        # need logic here
        self.grid[grid_position[0]][grid_position[1]].piece = piece

    def find_valid_moves(self, grid_position):
        piece = self.grid[grid_position[0]][grid_position[1]].piece
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

    def set_knights(self):
        for x in STARTING_COLUMNS.knight:
            self.grid[STARTING_ROWS.white_pieces][x].piece = knight(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = knight(
                team_name='black')

    def set_rooks(self):
        for x in STARTING_COLUMNS.rook:
            self.grid[STARTING_ROWS.white_pieces][x].piece = rook(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = rook(
                team_name='black')

    def set_bishops(self):
        for x in STARTING_COLUMNS.bishop:
            self.grid[STARTING_ROWS.white_pieces][x].piece = bishop(
                team_name='white')
            self.grid[STARTING_ROWS.black_pieces][x].piece = bishop(
                team_name='black')

    def set_yas_queens(self):
        self.grid[STARTING_ROWS.white_pieces][STARTING_COLUMNS.queen].piece = queen(
            team_name='white')
        self.grid[STARTING_ROWS.black_pieces][STARTING_COLUMNS.queen].piece = queen(
            team_name='black')

    def set_short_kings(self):
        self.grid[STARTING_ROWS.white_pieces][STARTING_COLUMNS.king].piece = king(
            team_name='white')
        self.grid[STARTING_ROWS.black_pieces][STARTING_COLUMNS.king].piece = king(
            team_name='black')
