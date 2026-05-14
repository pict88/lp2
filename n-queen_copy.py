N = 4

board = [[0 for i in range(N)] for j in range(N)]

# Function to check if queen can be placed
def is_safe(row, col):

    # Check left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower-left diagonal
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

# Backtracking function
def solve(col):

    # All queens placed
    if col >= N:
        return True

    for row in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(col + 1):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Solve the problem
if solve(0):

    print("Solution Found:\n")

    for row in board:
        print(row)

else:
    print("No Solution")