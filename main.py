# Tic-Tac-Toe By Yahbouss
#   1 | 2 | 3
#   --|---|--
#   4 | 5 | 6
#   --|---|--
#   7 | 8 | 9
# X / O

import time


def basic(ttt):
    print(f'''
    {ttt[0]} | {ttt[1]} | {ttt[2]}
    --|---|--
    {ttt[3]} | {ttt[4]} | {ttt[5]}
    --|---|--
    {ttt[6]} | {ttt[7]} | {ttt[8]}
    ''')


def initt():
    print('Welcome To Tic Tac Toe BY Yah Bouss')
    time.sleep(1)


def get_pos(symbol):
    try:
        pos = int(input(f'your move as {symbol} (1-9): '))
    except ValueError:
        pos = 666
    return pos


def choice_check(pos, ttt):
    if pos in range(0, 9):
        if ttt[pos] != "X" and ttt[pos] != "O":
            return True
    else:
        return False


def win_check(ttt, symbol):
    if (((ttt[0] == ttt[1]) & (ttt[1] == ttt[2])) |
            ((ttt[3] == ttt[4]) & (ttt[4] == ttt[5])) |
            ((ttt[6] == ttt[7]) & (ttt[7] == ttt[8])) |
            ((ttt[0] == ttt[3]) & (ttt[3] == ttt[6])) |
            ((ttt[1] == ttt[4]) & (ttt[4] == ttt[7])) |
            ((ttt[2] == ttt[5]) & (ttt[5] == ttt[8])) |
            ((ttt[0] == ttt[4]) & (ttt[4] == ttt[8])) |
            ((ttt[2] == ttt[4]) & (ttt[4] == ttt[6]))):
        print(f'You won {symbol} ! \nGame Over')
        return False
    else:
        return True


def turn_check(i):
    if i % 2 == 0:
        return 'O'
    elif i % 2 == 1:
        return 'X'


# main program

initt()
ttt = [1, 2, 3, 4, 5, 6, 7, 8, 9]
basic(ttt)
i = 1
symbol = 'X'
while win_check(ttt, symbol):
    symbol = turn_check(i)
    pos = get_pos(symbol) - 1
    if choice_check(pos, ttt):
        ttt[pos] = symbol
        basic(ttt)
        i = i + 1
    else:
        print('Wrong choice! Try again')

exit(666)