import pytest
from battleship.board import Board

def test_get_sequence():
    board = Board()
    board[0][0] = 'C'
    board[1][0] = 'C'

    assert board.get_sequence(0, 0, 3, 'NS') == ['C', 'C', 'S']
    assert board.get_sequence(0, 0, 2, 'EW') == ['C', 'S']

def test_collides_ns():
    board = Board()
    board[0][0] = 'C'
    board[1][0] = 'C'

    ship = {'size': 2}
    assert board.collides(0, 0, ship, 'NS')
    assert not board.collides(1, 0, ship, 'NS')


def test_collides_ew():
    board = Board()
    board[2][2] = 'C'
    board[2][3] = 'C'

    ship = {'size': 3}
    assert board.collides(0, 2, ship, 'EW')
    assert not board.collides(4, 2, ship, 'EW')


def test_place_ship_ns():
    board = Board()
    ship = {'letter': 'C', 'size': 2}

    board.place_ship(0, 0, ship, 'NS')
    assert board[0][0] == 'C'
    assert board[1][0] == 'C'


def test_place_ship_ew():
    board = Board()
    ship = {'letter': 'C', 'size': 2}

    board.place_ship(0, 0, ship, 'EW')
    assert board[0][0] == 'C'
    assert board[0][1] == 'C'


def test_place_ship_exc():
    board = Board()
    ship = {'letter': 'C', 'size': 2}

    with pytest.raises(IndexError) as excinfo:
        board.place_ship(0, 9, ship, 'NS')
    assert 'index out of range' in str(excinfo.value)
