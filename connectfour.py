from copy import deepcopy
import numpy as np

ROWS = 6
COLUMNS = 7

EMPTY = 0
RED = 1
BLUE = 2


class game:
    def setup(self):
        self.turn = RED
        self.board = np.zeros((ROWS, COLUMNS), np.int8)
        self.moves = np.full(COLUMNS, ROWS, np.int8)
        self.history = []


    def __init__(self, _id=None, player1=None, player2=None):
        self.setup()
        self._id = _id
        self.player1 = player1
        self.player2 = player2


    def set_id(self, number):
        self._id = number


    def get_id(self):
        return self._id


    def set_player1(self, player1):
        self.player1 = player1


    def get_player1(self):
        return self.player1


    def get_player2(self):
        return self.player2


    def set_player2(self, player2):
        self.player2 = player2


    def get_board(self):
        return self.board


    def check_win(self):
        def check(line, piece):
            win = False

            for tile in line:
                if item == piece:
                    score += 1
                    if score == 4:
                        win = True
                        break
                else:
                    score = 0

            return win


        def check_rows(board, piece):
            win = False
            search = np.sum(board, axis=1)

            index = 0
            for line in self.board:
                if search[index] > piece*4: # at least four pieces in play
                    if check(line, piece):
                        win = True
                        break

                index += 1
            
            return win


        def check_columns(board, piece):
            win = check_rows(board.transpose(), piece)

            return win


        def check_diagonals(board, piece):
            win = False

            slicer = np.arange(-2,4)
            # check left diagonal
            for index in slicer:
                line = np.diagonal(board, index)

                if np.sum(line) > piece*4: # at least four pieces in play
                    if check(line, piece):
                        win = True
                        break

            if win: # if winning move found, return
                return win

            # check right diagonal
            flip = np.fliplr(board)
            for index in slicer:
                line = np.diagonal(flip, index)

                if np.sum(line) > piece*4: # at least four pieces in play
                    if check(line, piece):
                        win = True
                        break

            return win


        board = deepcopy(self.board)
        if check_rows(board, RED) or check_columns(board, RED) or check_diagonals(board, RED):
            return RED
        elif check_rows(board, BLUE) or check_columns(board, BLUE) or check_diagonals(board, BLUE):
            return BLUE
        else:
            return False


    def make_move(self, column, piece):
        self.turn = self.turn%2 + 1 # toggles between the two turns

        if self.moves[column] == 0:
            return False
        else:
            self.board[self.moves[column]-1, column] = piece
            self.moves[column] -= 1
            self.history.append(column)
            return True
        

    def get_history(self):
        return self.history
    
        
    def update(self, input_history):
        if self.history == input_history:
            return False
        else:
            piece = RED

            self.setup()
            for move in input_history:
                self.make_move(move, piece)

            return True

    #def play(self):
        


def play_game():
    g = game()

    g.make_move(3, RED)
    g.make_move(3, RED)
    g.make_move(3, RED)
    g.make_move(3, RED)
    g.make_move(3, RED)
    g.make_move(3, RED)
    g.make_move(3, BLUE)
    g.make_move(3, BLUE)
    g.make_move(3, BLUE)
    g.make_move(3, BLUE)
    g.make_move(3, BLUE)
    g.make_move(3, BLUE)

    print g.board


if __name__ == '__main__':
    play_game()
