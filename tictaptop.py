# Tic Tac Toe Game in Python

# Function to print the board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(s == player for s in row):
            return True
    for col in range(3):
        if all(row[col] == player for row in board):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the board is full
def is_draw(board):
    return all(cell != " " for row in board for cell in row)

# Main game function
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))
        except ValueError:
            print("Invalid input! Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position! Try again.")
            continue
        if board[row][col] != " ":
            print("Position already taken! Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Congratulations! Player {current_player} wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()