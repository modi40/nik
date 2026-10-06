def check_winner(board):
    win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for a, b, c in win_lines:
        if board[a] == board[b] == board[c] and board[a] != ' ':
            return board[a]
    if ' ' not in board:
        return 'Tie'
    return None

def minimax(board, depth, is_maximizing):
    result = check_winner(board)
    if result == 'X':
        return 10 - depth
    elif result == 'O':
        return depth - 10
    elif result == 'Tie':
        return 0

    if is_maximizing:
        best_val = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                val = minimax(board, depth + 1, False)
                board[i] = ' '
                best_val = max(best_val, val)
        return best_val
    else:
        best_val = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                val = minimax(board, depth + 1, True)
                board[i] = ' '
                best_val = min(best_val, val)
        return best_val

def find_best_move(board):
    best_val = -float('inf')
    best_move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'X'
            move_val = minimax(board, 0, False)
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

def print_board(board):
    print(f' {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} ')

if __name__ == '__main__':
    current_board = [
        'X', 'O', 'X',
        'O', 'O', ' ',
        ' ', 'X', ' '
    ]
    print('TIC-TAC-TOE USING MINIMAX ALGORITHM')
    print('Current Board Configuration:')
    print_board(current_board)
    
    optimal_idx = find_best_move(current_board)
    print(f'\nComputer (X) chooses optimal position: {optimal_idx}')
    current_board[optimal_idx] = 'X'
    print('\nBoard After Computer Move:')
    print_board(current_board)
