import sys

def solve_nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []
    solve_nqueens_util(n, 0, board, solutions)
    print_solutions(solutions)

def solve_nqueens_util(n, row, board, solutions):
    if row == n:
        solutions.append([''.join(row) for row in board])
        return

    for col in range(n):
        if is_safe(row, col, board, n):
            board[row][col] = 'Q'
            solve_nqueens_util(n, row + 1, board, solutions)
            board[row][col] = '.'

def is_safe(row, col, board, n):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < n:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

def print_solutions(solutions):
    for solution in solutions:
        for row in solution:
            print(row)
        print()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solve_nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
