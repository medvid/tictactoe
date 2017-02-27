import board
import player
import game
import interface
import utils

board = board.Board(3)
player1 = player.HumanPlayer("Human 1")
player2 = player.HumanPlayer("Human 2")
game = game.Game(player1, player2, board)
interface = interface.ConsoleInterface(game)
interface.mainloop()
