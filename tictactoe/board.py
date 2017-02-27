import event

class Board(object):
    def __init__(self, dim):
        self.__dim = dim
        self.updated = event.Event()
        self.reset()

    # enable indexing with board[y][x]
    def __getitem__(self, y):
        return self.__state[y]

    @property
    def dim(self):
        return self.__dim

    def reset(self):
        """ Reset the board to the default state """
        self.__state = [[None for y in range(self.dim)] for x in range(self.dim)]
        self.__last_elem = None

    def make_turn(self, x, y, elem):
        if x >= self.dim or y >= self.dim:
            raise IndexError
        if not self.is_free_cell(x, y):
            raise CellBusyError(x, y)
        self[y][x] = elem
        self.__last_elem = elem
        self.updated(x, y, elem)

    def is_free_cell(self, x, y):
        return self[y][x] is None

    def get_free_cells(self):
        return [[x, y] for x in range(self.dim) for y in range(self.dim) if self.is_free_cell(x, y)]

    def is_draw(self):
        return not any(self.is_free_cell(x, y)
            for x in range(self.dim)
            for y in range(self.dim))

    def is_win(self):
        if any(self.__has_elem_match(row) for row in self.__get_rows()):
            return True
        elif any(self.__has_elem_match(col) for col in self.__get_columns()):
            return True
        elif any(self.__has_elem_match(diag) for diag in self.__get_diags()):
            return True
        else:
            return False

    def __has_elem_match(self, seq):
        return all(item is self.__last_elem for item in seq)

    def __get_row(self, y):
        return self.__state[y]

    def __get_rows(self):
        return map(self.__get_row, range(self.dim))

    def __get_column(self, x):
        return map(lambda y: self.__state[y][x], range(self.dim))

    def __get_columns(self):
        return map(self.__get_column, range(self.dim))

    def __get_diags(self):
        yield map(lambda x: self.__state[x][x], range(self.dim))
        yield map(lambda x: self.__state[x][self.dim - x - 1], range(self.dim))


class CellBusyError(Exception):
    def __init__(self, x, y):
        self.x = x
        self.y = y
