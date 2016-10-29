DIRECTIONS = ('NS', 'EW')
SEA = 'S'
SHIPS = [
    {'type':'carrier','size': 5, 'code': 'C'},
    {'type': 'battleship', 'size': 4, 'code': 'B'},
    {'type': 'cruiser', 'size': 3, 'code': 'R'},
    {'type': 'submarine', 'size': 3, 'code': 'U'},
    {'type': 'destroyer', 'size': 2, 'code': 'D'},
]

class Board(object):
    def __init__(self):
        self.board = [[SEA for _ in range(10)] for _ in range(10)]

    def __getitem__(self, i):
        return self.board[i]

    def get_sequence(self, col, row, sequence_size, direction):
        if direction not in DIRECTIONS:
            raise ValueError("invalid direction use: {}".format(DIRECTIONS))

        sequence = {'values': [], 'indices': []}
        for _ in range(0, sequence_size):  # style note: _ for unnec var name
            sequence['values'].append(self.board[row][col])
            sequence['indices'].append((row, col))
            if direction == DIRECTIONS[0]:
                row += 1
            else:
                col += 1
        return sequence

    def place_ship(self, col, row, ship, direction):
        sequence = self.get_sequence(col, row, ship['size'], direction)
        if not collides(sequence):
            for r, c in sequence['indices']:
                self.board[r][c] = ship['code']


def collides(sequence):
    return not all([s == SEA for s in sequence['values']])
