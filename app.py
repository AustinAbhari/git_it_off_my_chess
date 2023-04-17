from flask import Flask, render_template
from src.models.pieces.piece import piece
from src.models.pieces.pawn import pawn
from src.models.pieces.king import king
from src.models.pieces.knight import knight
from src.models.pieces.bishop import bishop
from src.models.pieces.queen import queen
from src.models.board import board
from src.models.game import game
from string import Template

app = Flask(__name__)

PIECE_NAME_MAP = {
    'pawn': pawn,
    'king': king,
    'queen': queen,
    'knight': knight,
    'bishop': bishop,
}


@app.route("/")
def i_got_game():
    g = game()
    g.new_game()
    return render_template("grid.html", data=g.board.get_grid())


@app.route("/pieces/<string:piece_name>")
def gimme_dat_piece(piece_name):
    piece_class = PIECE_NAME_MAP[piece_name]
    my_piece = piece_class()

    # shitty debugging for moving in a direction for a piece - parameterize this later
    print(list(my_piece.move_x_spaces_in_direction(x=2)))
    name = my_piece.current_position
    moveset = my_piece.valid_moveset
    new = Template("<p>Hello, World! $name - my moves are $moveset</p>")
    return new.substitute(name=name, moveset=moveset)


@app.route("/bishop")
def bish_better_have_my_moola():
    b = board()
    b.setup_board()
    return "hello"
