from flask import Flask
from src.models.piece import piece

from string import Template


app = Flask(__name__)

PIECE_NAME_MAP = {
    'pawn': piece
}


@app.route("/")
def hello_world():
    my_piece = piece(starting_point = 'fuck you', valid_moveset=[1,1]) 
    name = my_piece.starting_point
    moveset = my_piece.valid_moveset
    new = Template("<p>Hello, World! $name - my moves are $moveset</p>")
    
    return new.substitute(name=name, moveset=moveset)


@app.route("/pieces/<string:piece_name>")
def gimme_dat_piece(piece_name):
    piece_class = PIECE_NAME_MAP[piece_name]
    my_piece = piece_class(starting_point='fuck you', valid_moveset=[1,1])
    name = my_piece.starting_point
    moveset = my_piece.valid_moveset
    new = Template("<p>Hello, World! $name - my moves are $moveset</p>")
    return new.substitute(name=name, moveset=moveset)
