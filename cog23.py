def solve_n_queens(n):

    board = [['.'] * n for _ in range(n)]

    def is_safe(row, col):

        # Check same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        i = row - 1
        j = col - 1

        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False

            i -= 1
            j -= 1

        # Check upper-right diagonal
        i = row - 1
        j = col + 1

        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False

            i -= 1
            j += 1

        return True

    def backtrack(row):

        # All queens have been placed
        if row == n:
            return True

        for col in range(n):

            if is_safe(row, col):

                # Choose
                board[row][col] = 'Q'

                # Explore
                if backtrack(row + 1):
                    return True

                # Undo
                board[row][col] = '.'

        return False

    backtrack(0)

    return board


board = solve_n_queens(4)

for row in board:
    print(' '.join(row))