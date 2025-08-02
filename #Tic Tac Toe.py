#Tic Tac Toe

# 1. Create game board
def create_board():
    board = []
    for _ in range(3):
        row = [' ', ' ', ' ']
        board.append(row)
    return board

# 2. Print game board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-----')

# 3. Make a move
def make_move(board, player, row, col):
    if board[row][col] == ' ':
        board[row][col] = player
        return True
    else:
        return False

# 4. Check winner
def check_winner(board, player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True

    # Check columns 
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False

# 5. Check draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# 6. Main game loop
def play_tic_tac_toe():
    board = create_board()
    current_player = 'X'

    while True:
        print_board(board)
        try:
            row = int(input(f'Player {current_player}, choose your row (0-2): '))
            col = int(input(f'Player {current_player}, choose your column (0-2): '))
        except ValueError:
            print("Invalid input. Please enter numbers between 0 and 2.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position. Try again.")
            continue

        if not make_move(board, current_player, row, col):
            print('Invalid move, try again.')
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f'Congratulations! Player {current_player} wins!')
            break

        elif check_draw(board):
            print_board(board)
            print('It\'s a draw!')
            break

        current_player = 'O' if current_player == 'X' else 'X'


play_tic_tac_toe()