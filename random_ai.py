import connectfour
import connectfour_client as client
import numpy as np

server = "http://127.0.0.1:5000"
game = client.ClientGame(server, "Carey")

while not game.check_win():
    if not game.my_turn():
        game.get_move()
    else:
        # Insert AI code here
        move = np.random.randint(0,7)
        game.send_move(move)
print "Game Over!"
print "Winner:", game.get_winner()
