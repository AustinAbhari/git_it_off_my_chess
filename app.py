from flask import Flask, render_template
from src.models.piece import piece
from src.models.pawn import pawn
from src.models.king import king
from src.models.queen import queen
from src.models.board import board
from string import Template

app = Flask(__name__)

PIECE_NAME_MAP = {
    'pawn': pawn,
    'king': king,
    'queen': queen
}


@app.route("/")
def hello_world():
    my_piece = piece(starting_point='fuck you', valid_moveset=[1, 1])
    name = my_piece.starting_point
    moveset = my_piece.valid_moveset
    new = Template("<p>Hello, World! $name - my moves are $moveset</p>")

    return new.substitute(name=name, moveset=moveset)


@app.route("/pieces/<string:piece_name>")
def gimme_dat_piece(piece_name):
    piece_class = PIECE_NAME_MAP[piece_name]
    my_piece = piece_class(starting_point='fuck you')

    # shitty debugging for moving in a direction for a piece - parameterize this later
    print(list(my_piece.move_x_spaces_in_direction(x=2)))
    name = my_piece.starting_point
    moveset = my_piece.valid_moveset
    new = Template("<p>Hello, World! $name - my moves are $moveset</p>")
    return new.substitute(name=name, moveset=moveset)


@app.route("/board")
def big_ol_chess_board():
    b = board()
    b.setup_board()
    return render_template("grid.html", data=b.get_grid())
