def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False
            
    r, c = row, col
    while r >= 0 and c >= 0:
        if board[r][c] == 1:
            return False
        r -= 1
        c -= 1
        
    r, c = row, col
    while r < n and c >= 0:
        if board[r][c] == 1:
            return False
        r += 1
        c -= 1
        
    return True

def solve_n_queens_backtracking(board, col, n, solutions):
    if col >= n:
        solutions.append([[cell for cell in row] for row in board])
        return True
        
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens_backtracking(board, col + 1, n, solutions)
            board[row][col] = 0

def main():
    n = 4
    board = [[0] * n for _ in range(n)]
    solutions = []
    
    solve_n_queens_backtracking(board, 0, n, solutions)
    
    print(f'{n}-QUEENS PROBLEM VIA BACKTRACKING')
    print(f'Total Valid Solutions Found: {len(solutions)}\n')
    
    for idx, sol in enumerate(solutions, 1):
        print(f'Solution {idx}:')
        for row in sol:
            print(' '.join('Q' if cell == 1 else '.' for cell in row))
        print()

if __name__ == '__main__':
    main()
