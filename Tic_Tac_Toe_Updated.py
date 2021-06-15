#GLOBAL VARIABLES
#These global variables set the initial conditions for all of the functions 
player_piece = "X"
winner = None
count = 0
game_still_going = True
#Tic-Tac_toe board is 3x3 with an underscore used as a placemarker for the X and Y inputs
board = ["-","-","-",

         "-","-","-",

         "-","-","-"]

def display_board():
    #indexing used to find the proper location of the underscore space holder and then add a vertical line in the correct positon
    #To create a proper board
    print(board[0] + " | " + board[1] + " | " + board[2])
    
    print(board[3] + " | " + board[4] + " | " + board[5])
    
    print(board[6] + " | " + board[7] + " | " + board[8])
    
display_board()

#Introduce the user to the rules of Tic Tac Toe
def Introduction():
    print(" \n\n ///////////////////////")
    print("WELCOME TO TIC-TAC-TOE")
    print("/////////////////////// \n")

    print("THE RULES OF TIC-TAC-TOE ARE: \n")
    print("PLAYING AS EITHER X OR O PLACE A PIECE DOWN IN ONE SPOT \n")
    print("ONCE YOU DO THIS YOUR TURN IS OVER \n")
    print("YOU AND YOUR OPPONET CONTINUE TO TAKE TURNS UNTIL ONE OF TWO THINGS HAPPEN \n")
    print("EITHER ONE OF YOU HAS THREE OF YOUR PIECES IN THE SAME COLUMN OR ROW OR IN A DIAGONAL \n")
    print("OR ALL OF THE SPACES GET USED BEFORE THIS HAPPENS \n")
    print("IF THE FIRST CASE HAPPENS THAN WE HAVE A WINNER \n")
    print("AND IF THE SECOND CASE HAPPENS THAN THE GAME ENDS IN A TIE \n")


Introduction()

#Create a function that determines the order and conditions of other functions
def game_order():

    display_board()

    #While the game is still happening want to continue to loop through game conditions until the loop is broken with a result
    while game_still_going:

        game(player_piece)

        win()

        tie()

        change_player()
    #Terminating condition
    if winner == "X" or winner == "O":
        print("The winner of the game is ... {0} ! ".format(winner))
    else:
        print("The game has ended in a tie")





# A function that takes the players through the inputs necessary to play the game done by selecting positions through each 
# iteration
def game():
    
    player_position = input("To place a piece enter a number from 1-9 based on the coordinate system \n : ")
    #count keeps track of the total moves, if the total moves resulting in a newly placed piece equal 9, meaning
    #the board is full with Xs and Os, the while loop ends and no more inputs are added
    count = 0
    while count < 9:
        #Tried to use range for this but had difficulty with the string inputs
        while player_position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            player_position = input("choice invalid please enter a valid input between 1-9:\n")
        
        #Have to subtract 1 because of the index position coordinate
        player_position = int(player_position) - 1
        
        # Another way of saying the board position is empty, which if this is the case the board at the given location will
        #Become the player piece and the count integer will increase by 1
        if board[player_position] != "X" or "O":
            board[player_position] = player_piece
            count += 1
        else: 
            # If the player chooses a position that is already occupied by a piece they will get an error and have to go again
            print("you can't go there, go again")

        print("You have chosen position {0}\n".format(player_position))
        display_board()
    


#Set all the possible conditions for a player to win. This includes having three of the same piece in a row, column
# or diagonal. Once this occurs the game is no longer occuring and so the variable game still going is now false
def win():
    global game_still_going
    #only loops while there is still no winner
    while winner == None:
        # row conditions
        # there is only a winner if all three pieces are the same not including blanks, or else the game would be over 
        # immediately
        if board[0] == board[1] == board[2] != "-": 
            winner == player_piece
            game_still_going = False
        elif board[3] == board[4] == board[5] != "-":
            winner = player_piece
            game_still_going = False
        elif board[6] == board[7] == board[8] != "-":
            winner = player_piece
            game_still_going = False
        # column conditions
        elif board[0] == board[3] == board[6] != "-":
            winner = player_piece
            game_still_going = False
        elif board[1] == board[4] == board[7] != "-":
            winner = player_piece
            game_still_going = False
        elif board[2] == board[5] == board[8] != "-":
            winner = player_piece
            game_still_going = False
        # diagonal conditions
        elif board[0] == board[4] == board[8] != "-":
            winner = player_piece
            game_still_going = False
        elif board[6] == board[4] == board[2] != "-":
            winner = player_piece
            game_still_going = False


# Create a function that goes over the conditions of a tie game
def tie():
    #input necessary global variables that are relevant to the function, including a count variable that starts at 0
    global game_still_going
    global count
    # once count reaches 9 the game is no longer going and a tie is returned
    if count = 9:
        game_still_going = False
    return





# player piece has to be changed after each turn 
def change_player():
    global player_piece
    if player_piece == "X":
        player_piece == "O"
    elif player_piece == "O":
        player_piece == "X"

    return

game()


