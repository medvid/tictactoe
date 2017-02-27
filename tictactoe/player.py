import board
import random

class Player(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        """ Player name """
        return self.__name


class HumanPlayer(Player):
    def grab_turn(self, board):
        return None


class RandomPlayer(Player):
    def grab_turn(self, board):
        return random.choice(board.get_free_cells())
