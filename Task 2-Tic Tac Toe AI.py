import math

board = [' '] * 9

def winner(p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(all(board[i] == p for i in w) for w in wins)

def draw():
    return ' ' not in board

def minimax(ai):
    if winner('O'): return 1
    if winner('X'): return -1
    if draw(): return 0

    best = -math.inf if ai else math.inf
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O' if ai else 'X'
            score = minimax(not ai)
            board[i] = ' '
            best = max(best, score) if ai else min(best, score)
    return best

def ai_move():
    best, move = -math.inf, -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(False)
            board[i] = ' '
            if score > best:
                best, move = score, i
    board[move] = 'O'

while True:
    print(board[:3], "\n", board[3:6], "\n", board[6:])
    x = int(input("Enter position (1-9): ")) - 1
    if board[x] == ' ':
        board[x] = 'X'
    if winner('X'):
        print("You Win!")
        break
    if draw():
        print("Draw!")
        break
    ai_move()
    if winner('O'):
        print("Computer Wins!")
        break