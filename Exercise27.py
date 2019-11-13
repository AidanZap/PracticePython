from typing import List
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


def user_turn(type: str, board: List):
    try:
        cordinates = input("Enter coordinates (ex: 1,3): ").split(',')
        x = int(cordinates[0]) - 1
        y = int(cordinates[1]) - 1
        if x < 0 or y < 0:
            raise Exception
        elif board[y][x] is not 0:
            print('Tile has already been claimed. Skipping turn.')
        else:
            board[y][x] = type
    except Exception:
        print("Error in format, skipping player turn as punishment.\n")
    return board


while True:
    print(user_turn('X', board))