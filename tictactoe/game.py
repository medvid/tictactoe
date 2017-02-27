import board
import player
import event

ELEM_X = False
ELEM_O = True

class Game(object):
    def __init__(self, player1, player2, board):
        self.__player1 = player1
        self.__player2 = player2
        self.__board = board
        self.__current_elem = ELEM_X
        self.win = event.Event()
        self.draw = event.Event()
        self.switch = event.Event()

    @property
    def player1(self):
        return self.__player1

    @property
    def player2(self):
        return self.__player2

    @property
    def board(self):
        return self.__board

    @property
    def current_player(self):
        if self.__current_elem == ELEM_O:
            return self.__player2
        else:
            return self.__player1

    def reset(self):
        self.__board.reset()
        self.__current_elem = ELEM_X

    def make_turn(self, x, y):
        self.board.make_turn(x, y, self.__current_elem)
        if self.__board.is_win():
            self.win(self.current_player)
        elif self.__board.is_draw():
            self.draw()
        self.__switch_player()

    def __switch_player(self):
        if self.__current_elem == ELEM_X:
            self.__current_elem = ELEM_O
        else:
            self.__current_elem = ELEM_X
        self.switch()
