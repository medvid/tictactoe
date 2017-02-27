import sys
import board
import player
import game
import tkinter
from tkinter import messagebox, font

class Interface(object):
    def __init__(self, game):
        self.__game = game
        self.__game.win += self.on_game_win
        self.__game.draw += self.on_game_draw
        self.board.updated += self.on_board_updated

    @property
    def game(self):
        return self.__game

    @property
    def board(self):
        return self.__game.board


class ConsoleInterface(Interface):
    def on_game_win(self, player):
        print("{} wins!".format(player.name))
        self.__ask_new_game()

    def on_game_draw(self):
        print("Draw!")
        self.__ask_new_game()

    def on_board_updated(self, x, y, elem):
        for y in range(0, self.board.dim):
            if y > 0:
                print('-' * (self.board.dim * 4 - 1))
            print(' ' + ' | '.join(map(self.__map_board_item, self.board[y])) + ' ' )
        print()

    def __ask_new_game(self):
        print()
        c = input("Start new game? (y/N)").strip().upper()
        if c == "Y":
            self.game.reset()
            return # back to mainloop
        elif c == "N" or c == "":
            print("Bye!")
            exit(0)
        else:
            print("Please enter either Y or N")

    def __map_board_item(self, item):
        if item is game.ELEM_X:
            return "X"
        elif item is game.ELEM_O:
            return "O"
        else:
            return " "

    def __input_turn(self):
        player_name = self.game.current_player.name
        return map(int, input("[{}] enter X Y: ".format(player_name)).split(' '))

    def __print_example(self):
        print("3x3 example:")
        print(" 0 0 | 1 0 | 2 0")
        print("-----------------")
        print(" 0 1 | 1 1 | 2 1")
        print("-----------------")
        print(" 0 2 | 1 2 | 2 2")
        print()

    def mainloop(self):
        self.__print_example()
        while True:
            try:
                turn = self.game.current_player.grab_turn(self.board)
                if turn is None: # player is unable to provide a turn automatically
                    x, y = self.__input_turn()
                else:
                    x, y = turn
                    print("[{}] enter X Y: {} {}".format(self.game.current_player.name, x, y))
                self.game.make_turn(x, y)
            except ValueError:
                print("Invalid input, expected two numbers separated by space")
            except IndexError:
                print("Value out of the board range")
            except board.CellBusyError as e:
                print("Cell {}.{} is busy".format(e.x, e.y))


class TkinterInterface(Interface):
    pass
    # TODO
    # def __init__(self):
    #     self.__app = tkinter.Tk()
    #     self.__data = [[tkinter.StringVar() for x in range(self.__board.dim)] for y in range(self.__board.dim)]
    #     self.__player = tkinter.StringVar()
    #     self.__font = font.Font(size=36, weight=font.BOLD)
    #     self.__initialize_gui()
    #
    # def __initialize_gui(self):
    #     self.__reset()
    #
    #     self.__create_reset_button()
    #     self.__create_status_label()
    #     self.__create_cell_buttons()
    #
    #     app.title("TicTacToe")
    #     app.geometry("{}x{}+200+200".format(100 * dim + 10, 100 * dim + 60))
    #
    # def reset(self):
    #     [[data[x][y].set("") for x in range(dim)] for y in range(dim)]
    #
    # def grab_move(self, player_name):
    #     player_var.set(player_name)
    #
    # def check_values(values):
    #     if len(values) == 1:
    #         s = values.pop()
    #         if s:
    #             return True
    #     return False
    #
    # def win(player):
    #     messagebox.showinfo("Congratulations", "Player {} wins!".format("1" if player else "2"))
    #     reset()
    #
    # def solve(data):
    #     # check columns
    #     for i in range(dim):
    #         j_values = set()
    #         for j in range(dim):
    #             j_values.add(data[i][j].get())
    #         if check_values(j_values):
    #             return True
    #
    #     # check rows
    #     for j in range(dim):
    #         i_values = set()
    #         for i in range(dim):
    #             i_values.add(data[i][j].get())
    #         if check_values(i_values):
    #             return True
    #
    #     # check diagonals
    #     k_values = set()
    #     for k in range(dim):
    #         k_values.add(data[k][k].get())
    #     if check_values(k_values):
    #         return True
    #
    #     l_values = set()
    #     for l in range(dim):
    #         l_values.add(data[l][dim - l - 1].get())
    #     if check_values(l_values):
    #         return True
    #
    # # event handler
    #
    # def on_click(event, arg):
    #     global data, buttons, counter
    #     x=arg[0]
    #     y=arg[1]
    #     isplayer1 = counter % 2 == 0
    #     result = "X" if isplayer1 else "O"
    #     data[x][y].set(result)
    #     if solve(data):
    #         win(isplayer1)
    #     else:
    #         counter += 1
    #         player_var.set("Player {} movement".format("2" if isplayer1 else "1"))
    #
    # # Create GUI
    #
    # def create_reset_button():
    #     b = tkinter.Button(app, text = "Reset", command = reset, width = 10, height = 2)
    #     b.place(x = 5, y = 5)
    #
    # def create_status_label(player_var):
    #     l = tkinter.Label(app, textvariable = player_var, width = 20, height = 2)
    #     l.place(x = 100, y = 10)
    #
    # def create_cell_button(x, y, var):
    #     b = tkinter.Button(app, textvariable=var, width = 3, height = 1, font = font36)
    #     b.bind("<Button-1>", lambda event, arg=[x, y]: on_click(event, arg))
    #     b.place(x = x * 100 + 5 , y = y * 100 + 5 + 50)
    #
    # def create_cell_buttons():
    #     [[create_cell_button(x, y, data[x][y]) for x in range(dim)] for y in range(dim)]
    #
