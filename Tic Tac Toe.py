# ------------ Global Variables ------------

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# If Game is still going
game_still_going = True

# Default current player
current_player = "X"

# Who won / tie ?
winner = None

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def handle_turn(player):

    print(player + "'s turn")
    position = input("Choose a position from 1-9: ")

    valid = False

    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input. Choose a position from 1-9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there!")

    board[position] = player
    display_board()

def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():

    # Set up global variables
    global winner

    # Check all rows
    row_winner = check_rows()
    # Check all columns
    column_winner = check_columns()
    # Check all diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        # there was a winner
        winner = row_winner
    elif column_winner:
        # there was a winner
        winner = column_winner
    elif diagonal_winner:
        # there was a winner
        winner = diagonal_winner
    else:
        # there wasn't a winner
        winner = None

    return

def check_rows():
    # Setting up global variables
    global game_still_going

    # Check if all the rows have the same value
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row does have a match, then flag that there is a win, and end the game
    if row_1 or row_2 or row_3:
        game_still_going = False
    
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]

def check_columns():
    # Setting up global variables
    global game_still_going

    # Check if all the columns have the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column does have a match, then flag that there is a win, and end the game
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]

def check_diagonals():
    # Setting up global variables
    global game_still_going

    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False

    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return

def check_if_tie():
    # Set up global variables
    global game_still_going

    # Check if all boxes are full, and no winner
    if "-" not in board:
        game_still_going = False
        winner = None
        return winner
    return

def flip_player():
    # Set up global variables
    global current_player

    # Flip the player from X to O, or vice versa
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player="X"
    return

def play_game():
    # Display initial board
    display_board()

    while game_still_going:

        handle_turn(current_player)

        # Check if the game has ended
        check_if_game_over()

        # Flip the player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
        print(f"The winner is '{winner}' !'")
    elif  winner == None:
        print("Tie!")

play_game()
