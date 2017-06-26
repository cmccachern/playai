import connectfour
import requests
import numpy as np
import time


class ClientGame(connectfour.Game):
    def __init__(self, server, player_name):
        self.server = server
        self.move_url = server + "/connectfour/api/move"
        self.game_url = server + "/connectfour/api/game"
        # Join game
        self.player_name = player_name
        data = {"player": player_name}
        r = requests.post(self.server + "/connectfour/api/join", json=data)
        game_info = r.json()
        print game_info
        _id = game_info["id"]
        player1 = game_info["player1"]
        player2 = game_info["player2"]
        if player1 == self.player_name:#TODO: Potential issue if names are equal
            self.player = connectfour.RED
        elif player2 == self.player_name:
            self.player = connectfour.BLUE
        else: raise ValueError("player1: " + str(player1) + "; player2: " + str(player2))
        self._id = _id
        self.player1 = player1
        self.player2 = player2
        self.setup()
        #super(ClientGame, self).__init__(_id, player1, player2)
    
    def get_move(self):
        r = requests.get(self.game_url)
        json_board = r.json()
        history = json_board["history"]
        self.update(history)
        time.sleep(1)
    
    def send_move(self, move):
        player = None
        if self.player == connectfour.RED:
            player = "player1"
        elif self.player == connectfour.BLUE:
            player = "player2"
        if player == None:
            return
        move = {"move": move, "player":player}
        r = requests.post(self.move_url, json=move)
        json_board = r.json()
        print json_board
        history = json_board["history"]
        self.update(history)

    def my_turn(self):
        return self.player == self.turn

    def get_winner(self):
        if self.check_win() == connectfour.RED:
            return self.player1
        elif self.check_win() == connectfour.BLUE:
            return self.player2
        elif self.check_win() == True:
            return "Tie"
