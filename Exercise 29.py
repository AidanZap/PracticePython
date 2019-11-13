from typing import List


board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]


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


def check_winner(board):
    winner = 0
    if board[0][0] == board[0][1] == board[0][2]:
        if board[0][0] is not 0:
            return True
    elif board[1][0] == board[1][1] == board[1][2]:
        if board[1][0] is not 0:
            return True
    elif board[2][0] == board[2][1] == board[2][2]:
        if board[2][0] is not 0:
            return True
    elif board[0][0] == board[1][0] == board[2][0]:
        if board[0][0] is not 0:
            return True
    elif board[0][1] == board[1][1] == board[2][1]:
        if board[0][1] is not 0:
            return True
    elif board[0][2] == board[1][2] == board[2][2]:
        if board[0][2] is not 0:
            return True
    elif board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] is not 0:
            return True
    elif board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] is not 0:
            return True
    return False

def play_game():
    global board
    current_turn = 1

    while True:
        print(f"Player {current_turn}'s turn:\n")
        draw_board(3, 3, board)
        if current_turn == 1:
            board = user_turn(p1_type, board)
            current_turn = 2
        else:
            board = user_turn(p2_type, board)
            current_turn = 1
        if check_winner(board):
            draw_board(3, 3, board)
            if current_turn == 1:
                winner = 2
            else:
                winner = 1
            print(f"Player {winner} has won!")
            break
    return winner


winnings = {1: 0, 2: 0}
print("Welcome to Tic Tac Toe. \n------------------------\n")
response = input(f"Player 1, would you like to be X's or O's?: ")
if response.lower() == "o":
    p1_type = 'O'
    p2_type = 'X'
elif response.lower() == "x":
    p1_type = 'X'
    p2_type = 'O'
else:
    print("Not sure on your input.. I'll just make player 1 O's")
    p1_type = 'O'
    p2_type = 'X'
print(f"Great. Player 1 is {p1_type}s and Player 2 is {p2_type}s\n")
while True:
    winner = play_game()
    winnings[winner] += 1
    print(f'P1 Wins: {winnings[1]}\nP2 Wins: {winnings[2]}\n')
    response = input("Play again? (y/n)")
    if response.lower() == 'y':
        board = [[0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    elif response.lower() == 'n':
        break
    else:
        print("Did not understand response, exiting game.")
        break