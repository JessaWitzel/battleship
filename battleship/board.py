DIRECTIONS = ('NS', 'EW')
OCEAN = 'O'


class Board(object):
    def __init__(self):
        self.board = [[OCEAN for _ in range(10)] for _ in range(10)]
        self.hit_ships = []

    def __getitem__(self, i):
        return self.board[i]

    def attack(self, row, col):
        spot = self.board[row][col]
        if spot != OCEAN:
            self.board[row][col] = 'H'
            self.hit_ships.append(spot)
            return "Hit! {}:{}".format(row, col)
        else:
            self.board[row][col] = 'M'
            return "Miss. {}:{}".format(row, col)

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
    return not all([s == OCEAN for s in sequence['values']])
