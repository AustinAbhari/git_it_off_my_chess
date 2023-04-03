rows, cols = (8, 8)


class board:
    def __init__(self):
        self.white_turn = True
        self.grid = [[' ']*rows for _ in range(cols)]
        self.move_order = []

    def get_grid(self):
        return self.grid

    def setup_board(self):
        # Nasty looking prolly put in another file never to be seen again
        white_starting_row = 0
        black_starting_row = 7
        # Pawns
        for i in range(0, cols):
            self.grid[1][i] = "wP"
            self.grid[6][i] = "bP"

        # Knights
        knight_starting_columns = [1, 6]
        self.grid[white_starting_row][knight_starting_columns[0]] = "wKn"
        self.grid[white_starting_row][knight_starting_columns[1]] = "wKn"

        self.grid[black_starting_row][knight_starting_columns[0]] = "bKn"
        self.grid[black_starting_row][knight_starting_columns[1]] = "bKn"

        # Rooks
        rook_starting_columns = [0, 7]
        self.grid[white_starting_row][rook_starting_columns[0]] = "wR"
        self.grid[white_starting_row][rook_starting_columns[1]] = "wR"

        self.grid[black_starting_row][rook_starting_columns[0]] = "bR"
        self.grid[black_starting_row][rook_starting_columns[1]] = "bR"

        # Bishops
        bishop_starting_columns = [2, 5]
        self.grid[white_starting_row][bishop_starting_columns[0]] = "wB"
        self.grid[white_starting_row][bishop_starting_columns[1]] = "wB"

        self.grid[black_starting_row][bishop_starting_columns[0]] = "bB"
        self.grid[black_starting_row][bishop_starting_columns[1]] = "bB"

        # Queen
        queen_starting_column = 4
        self.grid[white_starting_row][queen_starting_column] = "wQ"
        self.grid[black_starting_row][queen_starting_column] = "bQ"

        # King
        king_starting_column = 3
        self.grid[white_starting_row][king_starting_column] = "wK"
        self.grid[black_starting_row][king_starting_column] = "bB"

        # once we get some hardware we need to update each square have an id and peice
        # prolly should be its own class

    def next_turn(self):
        # change turn to white or black, prolly move this is a game class
        # catalog in move order
        # re-call valid moves on each peice in the array
        self.white_turn = not self.white_turn

    def capture():
        # delete peice from grid
        # next_turn()
        return None

    def piece_move():
        # update grid
        # next_turn
        return None

    def print_board(self):
        print(self.grid)
