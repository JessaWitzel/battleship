import random


class Board(object):
    def __init__(self):
        self.board = [['S' for _ in range(10)] for _ in range(10)]

    def __getitem__(self, i):
        return self.board[i]

    def place_ship(self, col, row, ship, orientation):
        if not self.collides(col, row, ship, orientation):
            if orientation == 'NS':
                if row + ship['size'] > 9:
                    raise IndexError('ship too large to start on selected row')

                for ir, r in enumerate(self.board):
                    if ir >= row and ir <= row + ship['size']:
                        for ic, c in enumerate(r):
                            if ic == col:
                                self.board[ir][ic] = ship['letter']
            else:
                for ir, r in enumerate(self.board):
                    if ir == row:
                        for ic, c in enumerate(r):
                            if ic >= col and ic <= col + ship['size']:
                                self.board[ir][ic] = ship['letter']

    def collides(self, col, row, ship, orientation):
        if orientation == 'NS':
            for ir, r in enumerate(self.board):
                # are you on the starting row or any row that would be touched
                # from a ship of this size?
                if ir >= row and ir <= row + ship['size']:
                    for ic, c in enumerate(r):
                        # are we on the column?
                        if ic == col:
                            if self.board[ir][ic] != 'S':
                                return True
        else:
            for ir, r in enumerate(self.board):
                if ir == row:
                    for ic, c in enumerate(r):
                        if ic >= col and ic <= col + ship['size']:
                            if self.board[ir][ic] != 'S':
                                return True
        return False
