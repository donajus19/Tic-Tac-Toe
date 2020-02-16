# ---- Global variables ------
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

# if game is still going
game_still_going = True

# who won? or tie?

winner = None

#whos turn is it
current_player = "X"

# display board
def display_board():
    print(board[0] + " | " + board [1] + " | " + board[2])
    print(board[3] + " | " + board [4] + " | " + board[5])
    print(board[6] + " | " + board [7] + " | " + board[8])

# play game of tic tac toe
def play_game():
    #display initial board
    display_board()

    # while the game is still going
    while game_still_going:
        #handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_if_game_over()

        # Flip to another player
        flip_player() 
 
    #the game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("It's a tie")

# Handle a single turn of an arbitrary player
def handle_turn(current_player):

    print(current_player +"'s move")
    #propt the user to select the position 
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        #if position was not set to one of these position
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input. Choose a position from 1-9: ")

        #subtract 1 to fit the board array
        position = int(position) - 1

        # Check if this board position is available
        if board[position] == "-":
            #if so quit the loop and move to displaying player's choice on board
            valid = True
        else:
            print("You can't go there.")



    #display player's choice on the board
    board[position] = current_player
    #dispaly board
    display_board()

def check_if_game_over(): 
    check_for_winner()
    check_if_tie()

def check_for_winner():
    #set up global variable
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonals
    diagonal_winner = check_diagonals()
    
    # Get the winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner   
    else:
        winner = None


def check_rows():
    #set up global variables so that we can write to them
    global game_still_going
    #if all 3 in row 1 are equal, then set to true. make exception for dash, because it will think dash is a win
    #check if any rows have all the same value and is not empty 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-" 
    #if any row have a match, flag there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner X or O
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return None


def check_columns():
    #set up global variables
    global game_still_going

    # Check if any columns have all the same value
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any column does have a match, flag there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    
    # return winner X or O
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return None


def check_diagonals():
    # Set up global variables
    global game_still_going

    # Check if any diagonal have all the same value
    diagonal_1 = board[0] == board[4] == board [8] != "-"
    diagonal_2 = board[6] == board[4] == board [2] != "-"

    # if any diagonal does have a match, flag there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False
    
        #return winner X or O
        if diagonal_1:
            return board[0]
        elif diagonal_2:
            return board[6]
    return None

# Check if there is a dash, if there is, then there is no tie, but if there is no dash, 
# then all spaces have been filled and there is a tie
def check_if_tie():
    # set up global variable so that we can write to it
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    #set up global variables we need
    global current_player
    # if the current player was x, then change it to O
    if current_player == "X":
        current_player = "O"
    # if currnet player was o, change it to x
    elif current_player == "O":
        current_player = "X"
    return
play_game()

# board
# display board
# function to play game
# fucntion to check win
    #check rows
    #check columns 
    #check diagonals
# function to check tie
# flip
# handle a turn