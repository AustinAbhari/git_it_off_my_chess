from flask import Flask, render_template, request
from src.models.pieces.pawn import pawn
from src.models.pieces.king import king
from src.models.pieces.knight import knight
from src.models.pieces.bishop import bishop
from src.models.pieces.queen import queen
from src.models.pieces.rook import rook
from src.models.board import board
from src.models.game import Game
from src.util.valid_moves import valid_moves
from string import Template
from flask_cors import CORS
import json
from json import JSONEncoder
import numpy
import json

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

g = Game()
g.new_game()


@app.route("/game")
def gamer():
    return CoolEncoder().encode(g)


@app.route("/moves/<int:positionx>-<int:positiony>")
def another_cool_name(positionx, positiony):
    output = g.find_valid_moves(
        [positionx, positiony])
    return json.dumps(output, cls=NumpyArrayEncoder)


@app.route("/move", methods=['POST'])
def move_get_out_the_way():
    body = request.json
    f = [eval(i) for i in body.get('from')]
    t = [eval(i) for i in body.get('to')]
    g.validate_and_move(f, t)
    return CoolEncoder().encode(g)


@app.route("/")
def i_got_game():
    g = Game()
    g.new_game()
    return render_template("grid.html", data=g.board.get_grid())
