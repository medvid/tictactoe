import board
import player
import game
import interface
import utils

print("Select board size:")
board_size = utils.get_int()
board = board.Board(board_size)

print("Choose type of game:")
print("1 - Human vs Human")
print("2 - Human vs Random")
print("3 - Random vs Random")
game_type = utils.get_int(3)

if game_type == 1:
    player1 = player.HumanPlayer("Human 1")
    player2 = player.HumanPlayer("Human 2")
elif game_type == 2:
    player1 = player.HumanPlayer("Human")
    player2 = player.RandomPlayer("Random")
elif game_type == 3:
    player1 = player.RandomPlayer("Random 1")
    player2 = player.RandomPlayer("Random 2")
else:
    assert False, "Unexpected game type"

game = game.Game(player1, player2, board)

print("Select user interface:")
print("1 - Console")
print("2 - Tkinter")
ui_type = utils.get_int(2)
if ui_type == 1:
    interface = interface.ConsoleInterface(game)
elif ui_type == 2:
    interface = interface.TkInterface(game)
else:
    assert False, "Unexpected UI type"

interface.mainloop()
