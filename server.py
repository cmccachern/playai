#!flask/bin/python
import numpy as np
from flask import Flask, jsonify
from flask import abort, make_response, request
from flask.ext.httpauth import HTTPBasicAuth
import sys
auth = HTTPBasicAuth()

import connectfour

app = Flask(__name__)

# Start Game
_id = 1
game = connectfour.Game(_id)

# Assign Colors
players = {"player1":connectfour.RED, "player2":connectfour.BLUE}
#valid = game.make_move(col, piece)
#winner = game.check_win()
#game.get_board()

@app.route("/connectfour/api/join", methods=["POST"])
def join_game():
    # TODO: Check for player
    if not request.json or not "player" in request.json:
        print "Invalid request"
        abort(400)
    player = request.json["player"]
    if game.get_player1() == None:
        print "Player 1 has joined"
        game.set_player1(player)
    elif game.get_player2() == None:
        game.set_player2(player)
    else: # Game is full
        print "Game is Full"
        abort(400)
    return jsonify({"id": game.get_id(), "player1": game.get_player1(), "player2": game.get_player2()}), 201


#@app.route("/connectfour/api/tasks/<int:game_id>", methods=["GET"])
@app.route("/connectfour/api/game", methods=["GET"])
def get_board():
    return jsonify({"history": game.get_history()})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found"}), 404)

@app.route("/connectfour/api/move", methods=["POST"])
def make_move():
    # TODO: Check for player
    if not request.json or not "move" in request.json:
        abort(400)
    player = players[request.json["player"]]
    move = request.json["move"]
    success = game.make_move(move, player)
    if not success:
        abort(400)
    # Print game
    print game.get_board()
    return jsonify({"history": game.get_history()}), 201

def index():
    return ""

if __name__ == "__main__":
    app.run(debug=True)
