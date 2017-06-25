import numpy as np

ROWS = 6
COLUMNS = 7

EMPTY = 0
RED = 1
BLUE = 2


class game:
    def __init__(self):
        self.board = np.zeros((ROWS, COLUMNS), np.int8)
        self.moves = np.full(COLUMNS, ROWS, np.int8)


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


        def check_rows(self, piece):
            search = np.sum(self.board, axis=1)

            for line in self.board:
                index = 0

                if search[index] > 4:
                    if check(line, piece):
                        break
            

    def make_move(self, column, piece):
        if self.moves[column] == 0:
            print 'Invalid Move'
            return -1
        else:
            self.board[self.moves[column]-1, column] = piece
            self.moves[column] -= 1
            return 0

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
