#create a blank board
board = [['-','-','-']
        ,['-','-','-']
        ,['-','-','-']]

#create a function that prints the board
def printBoard():
        print(board[0])
        print(board[1])
        print(board[2])

#create a function to check if the square is empty or the input is valid
def valid_move(row, col, game_piece):
    try:
        while board[row][col] == "X" or board[row][col]=="O":
            print("That spot is already filled.")
            printBoard()
            if game_piece == "X":
                row = int(input("Player 1 - Enter a row (1-3): ")) -1
                col = int(input("Player 1 - Now enter a column (1-3): ")) -1
            elif game_piece == "O":
                row = int(input("Player 2 - Enter a row (1-3): ")) -1
                col = int(input("Player 2 - Now enter a column (1-3): ")) -1
        else:
            update_board(row, col, game_piece)
    except IndexError:
        print("That is not a valid spot on the board.")
        printBoard()
        if game_piece == "X":
            row = int(input("Player 1 - Enter a row (1-3): ")) -1
            col = int(input("Player 1 - Now enter a column (1-3): ")) -1
        elif game_piece == "O":
            row = int(input("Player 2 - Enter a row (1-3): ")) -1
            col = int(input("Player 2 - Now enter a column (1-3): ")) -1

def update_board(row, col, game_piece):
    board[row][col] = game_piece


#game variables
turn = 0
game_piece = "X"
game_over = False

#Game Loop

#show board
printBoard()

#have the players take turns entering a position on the board to fill
#by entering a row and column to choose the specific box to fill
#add a -1 after each entry to keep track of the amount of moves
while not game_over:
    #player 1's move
    if turn == 0:
        row = int(input("Player 1 - Enter a row (1-3): ")) -1
        col = int(input("Player 1 - Now enter a column (1-3): ")) -1
        valid_move(row, col, game_piece)
        printBoard()
    #player 2's move
    if turn == 1:
        row = int(input("Player 2 - Enter a row (1-3): ")) -1
        col = int(input("Player 2 - Now enter a column (1-3): ")) -1
        valid_move(row, col, game_piece)
        printBoard()
    #alternate players
    #this sets up the if statements above that determine what player is playing
    #turn was oringailly defined and initialized as 0
    #after the 2nd if statement turn == 1
    #turn + 1 = 2 = turn
    #turn % 2 = 0 -- resetting at the first if statement
    turn += 1
    turn = turn % 2

    #if the game piece just used was "X" then switch to "O"
    #otherwise use "X"
    if game_piece == 'X':
        game_piece = 'O'
    else:
        game_piece = 'X'

