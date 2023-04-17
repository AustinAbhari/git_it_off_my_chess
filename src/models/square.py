class square:
    def __init__(self, color=None):
        # self.name = name
        self._piece = None
        self._color = None

    def set_piece(self, piece):
        self._piece = piece

    def get_piece(self):
        return self._piece

    def del_piece(self):
        self._piece = None

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color

    def del_color(self):
        self._color = None

    def show_piece_representation(self):
        return self._piece == ' ' if None else self.peice.team_piece_representation()

    piece = property(get_piece, set_piece, del_piece)
    color = property(get_color, set_color, del_color)
