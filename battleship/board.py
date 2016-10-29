import random


class Board(object):
    def __init__(self):
        self.board = [['S' for _ in range(10)] for _ in range(10)]

    def __getitem__(self, i):
        return self.board[i]

    def get_sequence(self, col, row, sequence_size, direction):
        sequence_values = []
        if direction == 'NS':
            for _ in range(0, sequence_size): #style note: _ for unnec var name
                sequence_values.append(self.board[row][col])
                row += 1
        elif direction == 'EW':
            for _ in range(0, sequence_size):
                sequence_values.append(self.board[row][col])
                col += 1
        else:
            raise ValueError("Please use a valid direction: 'NS' or 'EW'.")
        return sequence_values

    def place_ship(self, col, row, ship, orientation):
        if not self.collides(col, row, ship, orientation):
            if orientation == 'NS':
                for _ in range(0, ship['size']):
                    self.board[row][col] = ship['letter']
                    row += 1
            else:
                for _ in range(0, ship['size']):
                    self.board[row][col] = ship['letter']
                    col += 1

    def collides(self, col, row, ship, orientation):
        sequence_values = self.get_sequence(col, row, ship['size'], orientation)
        if 'C' in sequence_values:
            return True
        else:
            return False
