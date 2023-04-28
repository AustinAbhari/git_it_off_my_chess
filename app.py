from flask import Flask, render_template, jsonify
from src.models.pieces.pawn import pawn
from src.models.pieces.king import king
from src.models.pieces.knight import knight
from src.models.pieces.bishop import bishop
from src.models.pieces.queen import queen
from src.models.pieces.rook import rook
from src.models.board import board
from src.models.game import game
from src.util.valid_moves import valid_moves
from string import Template
from flask_cors import CORS
import json
from json import JSONEncoder
import numpy

app = Flask(__name__)
CORS(app)


class CoolEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


PIECE_NAME_MAP = {
    'pawn': pawn,
    'king': king,
    'queen': queen,
    'knight': knight,
    'bishop': bishop,
    'rook': rook
}

g = game()
g.new_game()


@app.route("/game")
def gamer():
    return CoolEncoder().encode(g)


@app.route("/moves/<int:positionx>-<int:positiony>")
def another_cool_name(positionx, positiony):
    output = g.board.find_valid_moves(
        [positionx, positiony])
    print(output)
    return json.dumps({'moves': output}, cls=NumpyArrayEncoder)


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


@app.route("/moves/<string:piece_name>/<string:team>/<int:positionx><int:positiony>")
def bishop_better_have_my_moola(piece_name, team, positionx, positiony):
    piece_class = PIECE_NAME_MAP[piece_name]
    grid_position = [positionx, positiony]
    my_piece = piece_class(team_name=team)
    moves = my_piece.get_valid_moveset()

    b = board()
    b.move_piece(my_piece, grid_position)

    valid_moves_set = valid_moves(moves, grid_position)
    b.display_valid_moves(valid_moves_set)

    return render_template("grid.html", data=b.get_grid())
