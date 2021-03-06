DIRECTIONS = ('NS', 'EW')
OCEAN = 'O'
##Doing this to show Geoff how to push things

class Board(object):
    def __init__(self):
        self.board = [[OCEAN for _ in range(10)] for _ in range(10)]
        self.hit_ships = []
        self.sank_ships = []

    def __getitem__(self, i):
        return self.board[i]

    def attack(self, row, col):
        spot = self.board[row][col]
        if spot == 'H':
            return "You have already fired and hit a ship at that location. Try again."
        elif spot != OCEAN:
            self.board[row][col] = 'H'
            self.hit_ships.append(spot)
            return "Hit! {}:{}".format(row, col)
        else:
            self.board[row][col] = 'M'
            return "Miss. {}:{}".format(row, col)

    def get_sequence(self, start_col, start_row, ship_size, direction):
        if direction not in DIRECTIONS:
            raise ValueError("invalid direction use: {}".format(DIRECTIONS))

        sequence = {'values': [], 'indices': []}
        for _ in range(0, ship_size):  # style note: _ for unnec var name
            sequence['values'].append(self.board[start_row][start_col])
            sequence['indices'].append((start_row, start_col))
            if direction == DIRECTIONS[0]:
                start_row += 1
            else:
                start_col += 1
        return sequence

    def place_ship(self, col, row, ship, direction):
        sequence = self.get_sequence(col, row, ship['size'], direction)
        if not collides(sequence):
            for r, c in sequence['indices']:
                self.board[r][c] = ship['code']

    def user_place(self):
        for ship in ships:
            print "Where would you like to place your %s?" %ship['type']
            col = raw_input['Column: ']
            row = raw_input['Row: ']
            choice = raw_input['Do you want to orient that ship North/South?']
            if 'y' in choice:
                direction = 'NS'
            else:
                direction = 'EW'
            return self.place_ship(col, row, ship[type], direction)

    def sank(self, ship):
        if self.hit_ships.count(ship['code']) == ship['size']:
            return "You sank my %s!" %ship['type']
            sank_ships.append(ship['code'])
            return end_game()

    def end_game(self):
        if len(self.sank_ships) == 5:
            return "That was my last ship! You win!"
            quit()


def collides(sequence):
    return not all([s == OCEAN for s in sequence['values']])
