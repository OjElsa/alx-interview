import sys

def is_safe(row, col, cols):
    # Check row and diagonal conflicts
    for i in range(col):
        if cols[i] == row or abs(row - cols[i]) == abs(col - i):
            return False
    return True

def solve_n_queens(n, cols):
    if len(cols) == n:
        print_solution(cols)  # Optional: Print a solution
        return

    for row in range(n):
        if is_safe(row, len(cols), cols):
            cols.append(row)
            solve_n_queens(n, cols)
            cols.pop()  # Backtrack

def print_solution(cols):
    # Implement chessboard visualization (optional)
    pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)


