board = [[1, 1, 0],
         [1, 2, 0],
         [2, 2, 2]]

def check_winner(board):
    winner = 0
    if board[0][0] == board[0][1] == board[0][2]:
        winner =  board[0][0]
    elif board[1][0] == board[1][1] == board[1][2]:
        winner = board[1][0]
    elif board[2][0] == board[2][1] == board[2][2]:
        winner = board[2][0]
    elif board[0][0] == board[1][0] == board[2][0]:
        winner = board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]:
        winner = board[0][1]
    elif board[0][2] == board[1][2] == board[2][2]:
        winner = board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]:
        winner = board[0][0]
    elif board[0][2] == board[1][1] == board[2][0]:
        winner = board[0][2]

    if winner == 0:
        return False
    return winner

print(check_winner(board))