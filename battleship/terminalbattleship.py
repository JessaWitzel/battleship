from random import randint

game_board = []
#create a list of lists of 0s
for x in range(0,5):
    game_board.append(['0'] * 5)

def print_board(board):
    for row in board:
        print ' '.join(row)

def game():
    turns = int(raw_input('How many turns would you like? '))
    for x in range(0,turns):
        print "This is turn: " + str(x + 1)
        print_board(game_board)
        print "Tell us what row and column you think the ship is hiding in."
        guess_row = int(raw_input("Row: "))
        guess_col = int(raw_input("Column: "))
        battle(guess_row, guess_col, x)

ship_row = randint(1,5)
ship_col = randint(1,5)

def battle(row, column, x):
    if row == ship_row and column == ship_col:
        print "You sunk my battleship!"
        exit()
    elif game_board[row - 1][column - 1] == '0':
        print "There is no ship there."
        game_board[row - 1][column - 1] = 'X'
    elif game_board[row - 1][column - 1] == 'X':
        print "You already guessed that. Try again!"

game()
