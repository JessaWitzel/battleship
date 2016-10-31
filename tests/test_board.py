import pytest
from battleship.board import (
    Board,
    collides,
)


def test_get_sequence():
    board = Board()
    board[0][0] = 'C'
    board[1][0] = 'C'

    ns_seq = board.get_sequence(0, 0, 3, 'NS')
    assert ns_seq == {'values': ['C', 'C', 'O'],
                      'indices': [(0, 0), (1, 0), (2, 0)]}

    ew_seq = board.get_sequence(0, 0, 2, 'EW')
    assert ew_seq == {'values': ['C', 'O'],
                      'indices': [(0, 0), (0, 1)]}


def test_get_sequence_exc():
    board = Board()
    with pytest.raises(ValueError) as excinfo:
        board.get_sequence(0, 0, 2, 'SE')
    assert 'invalid direction' in str(excinfo.value)


def test_collides_false():
    sequence = {'values': ['O', 'O', 'O']}
    assert not collides(sequence)


def test_collides_true():
    sequence = {'values': ['O', 'O', 'C']}
    assert collides(sequence)


def test_place_ship_ns():
    board = Board()
    ship = {'code': 'C', 'size': 2}

    board.place_ship(0, 0, ship, 'NS')
    assert board[0][0] == 'C'
    assert board[1][0] == 'C'


def test_place_ship_ew():
    board = Board()
    ship = {'code': 'C', 'size': 2}

    board.place_ship(0, 0, ship, 'EW')
    assert board[0][0] == 'C'
    assert board[0][1] == 'C'


def test_place_ship_exc():
    board = Board()
    ship = {'code': 'C', 'size': 2}

    with pytest.raises(IndexError) as excinfo:
        board.place_ship(0, 9, ship, 'NS')
    assert 'index out of range' in str(excinfo.value)


def test_attack_hit():
    board = Board()
    board[0][0] = 'C'
    board[0][1] = 'C'

    result = board.attack(0, 0)
    assert result == 'Hit! 0:0'
    assert board[0][0] == 'H'
    assert board.hit_ships == ['C']


def test_attack_miss():
    board = Board()

    result = board.attack(0, 1)
    assert result == 'Miss. 0:1'
    assert board[0][1] == 'M'
    assert board.hit_ships == []
