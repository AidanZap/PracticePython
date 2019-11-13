from typing import List

board = [[0, 0, 'X'],
         [0, 'X', 0],
         ['X', 0, 0]]


def draw_board(length: int, width: int, board: List):
    hor = ' --- '
    ver = '| {}  '

    print(hor * length)
    for y in range(0, width):
        for x in range(0, length):
            if board[y][x] is not 0:
                print(ver.format(board[y][x]), end="")
            else:
                print(ver.format(" "), end="")
        print("|")
        print(hor * length)

draw_board(3, 3, board)