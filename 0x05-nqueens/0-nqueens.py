#!/usr/bin/python3
import sys

def is_safe(row, col, queens):
    """Checks if placing a queen at (row, col) is safe (no conflicts).

    Args:
        row (int): Row index.
        col (int): Column index.
        queens (list): List of existing queen positions (row, col pairs).

    Returns:
        bool: True if safe, False otherwise.
    """
    # Check row and diagonal conflicts
    for q_row, q_col in queens:
        if q_row == row or abs(row - q_row) == abs(col - q_col):
            return False
    return True

def solve_n_queens(n):
    """Solves the N-queens problem and prints solutions.

    Args:
        n (int): Chessboard size (N x N).
    """
    solutions = []

    def backtrack(queens, row):
        """Recursive function to explore queen placements (backtracking).

        Args:
            queens (list): List of existing queen positions.
            row (int): Current row being explored.
        """
        if row == n:  # Base case: all queens placed (solution found)
            solutions.append(queens.copy())  # Add a copy to avoid modification
            return

        for col in range(n):
            if is_safe(row, col, queens):
                queens.append((row, col))
                backtrack(queens, row + 1)  # Explore next row
                queens.pop()  # Backtrack: remove queen if no solution found

    backtrack([], 0)  # Start with empty list, row 0

    if solutions:
        for sol in solutions:
            print(sol)  # Print each solution (list of queen positions)
    else:
        print("No solutions found for N =", n)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_n_queens(n)

