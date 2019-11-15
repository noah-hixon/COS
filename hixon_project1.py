








#checks to see if the user inputs a valid response
def validatePlayers(numOfPlayers):
    while numOfPlayers != "y" and numOfPlayers != "n":
        print("INVALID INPUT")
        numOfPlayers = input("Do you want the computer to be one player?[y/n]")
    
    if numOfPlayers == "y":
        print("You will play the computer.")
    elif numOfPlayers == "n":
        print("Both players will come from human input.")


# gets input from the user and validates it
def getInput():
    global ROWS # will be global variable
    global COLUMNS # will be global variable
    print("Welcome to Connect 4!\nCode By Noah Hixon\nThis game is for 2 players")
    numOfPlayers = str(input("Do you want the computer to be one player?[y/n]"))
    if numOfPlayers != "y" and numOfPlayers != "n":     # validates computer player input
        validatePlayers(numOfPlayers)
    elif numOfPlayers == "y":
        print("You will play the computer.")
    elif numOfPlayers == "n":
        print("Both players will come from human input.")
    print("The default board has 6 rows and 7 columns")
    ROWS = int(input("How many rows would you like? Please enter a number greater than or equal to 5:"))
    
    while ROWS < 5: # validates ROWS input
        print("You did not enter a valid number.")
        ROWS = int(input("How many rows would you like? Please enter a number greater than or equal to 5:"))
    
    COLUMNS = int(input("How many columns would you like? Please enter a number greater than or equal to 5:"))
    while COLUMNS < 5:  # validates COLUMNS input
        print("You did not enter a valid number")
        COLUMNS = int(input("How many columns would you like? Please enter a number greater than or equal to 5:"))

# creates board and returns it
def createBoard(ROWS, COLUMNS):
    BOARD = []
    for i in range(ROWS):
        temp = []
        for j in range(COLUMNS):
            temp.append("_ ")
        BOARD.append(temp)
    return BOARD



# prints the board
def printBoard(BOARD,COLUMNS):
    
    
    for row in range(len(BOARD)- 1, -1, -1):
        print(BOARD[row], "\n")
        
    


# checks to see if the user input a valid number for column
def validateColumns(columns):
    while columns > COLUMNS:
        print("That number is not valid")
        columns = int(input("Please choose a column to place your piece(1-" + str(COLUMNS) + "):"))


def dropPiece(board, row, col, piece):
    board[row][col - 1] = piece


def columnFull(board, column):
    if board[0][column] == "X" or board[0][column] == "O":
        print("COLUMN FULL\nEnter new column")
        return False
    else:
        return True

'''
def slotFull(board, column):
        if board[0][column] != "_":
            return False
        else:
            return True
'''



def slotFull(board, ROWS, column):
    
    for row in range(ROWS):
        if board[row][column-1] == "_ ":
            return row
    return -1

def getRow(board, column):
    pass




def checkWin(board, playPiece):
    
    for col in range(COLUMNS-3): # this checks horizontally for win
        for row in range(ROWS):
            if board[row][col] == playPiece and board[row][col + 1] == playPiece and board[row][col+2] == playPiece and board[row][col + 3] == playPiece:
            
                return True
 

    for col in range(COLUMNS): # this check vertically for win
        for row in range(ROWS - 3):
            if board[row][col] == playPiece and board[row + 1][col] == playPiece and board[row + 2][col] == playPiece and board[row + 3][col] == playPiece:
                return True

    for col in range(COLUMNS -3): # this checks diagonally (positive) for win
        for row in range(ROWS - 3):
            if board[row][col] == playPiece and board[row + 1][col + 1] == playPiece and board[row + 2][col + 2] == playPiece and board[row + 3][col + 3] == playPiece:
                return True

    return False

# main game loop
def main():
    gameWon = False
    turn = 0
    
    getInput()
    board = createBoard(ROWS, COLUMNS)
    printBoard(board, COLUMNS)


    while not gameWon:
        if turn%2 == 0:
            piece = "X"
            print("Player 1, what is your choice?")
            choice = int(input("Choose a column to drop your piece:"))
        
            if choice < 1 or choice > COLUMNS:
                choice = validateColumns(choice)

        
            else:
                if slotFull(board,ROWS, choice) == -1:
                    choice = int(input("COLUMN FULL\nEnter a new column:"))
                else:
                    row = slotFull(board, ROWS, choice)
                    dropPiece(board, row, choice, piece)
                    printBoard(board, COLUMNS)
         
            gameWon = checkWin(board, "X")
            turn += 1
            
        elif turn%2 == 1:
            piece = "O"
            print("Player 2, what is your choice?")
            choice = int(input("Choose a column to drop your piece:"))
            if choice < 1 or choice > COLUMNS:
                choice = validateColumns(choice)
            
            else:
                if slotFull(board,ROWS, choice) == -1:
                    choice = int(input("COLUMN FULL\nEnter a new column:"))
                    
                    
                else:
                    row = slotFull(board, ROWS, choice)
                    dropPiece(board, row, choice, piece)
                    printBoard(board, COLUMNS)
            gameWon = checkWin(board, "O")
            turn += 1

    print("You win")
main()

