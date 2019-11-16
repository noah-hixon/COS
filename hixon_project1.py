import random




#checks to see if the user inputs a valid response
def validatePlayers(numOfPlayers):
    while numOfPlayers != "y" and numOfPlayers != "n":
        print("INVALID INPUT")
        numOfPlayers = input("Do you want the computer to be one player?[y/n]")
    
    if numOfPlayers == "y":
        print("You will play the computer.")
        return True
    elif numOfPlayers == "n":
        print("Both players will come from human input.")
        return False

# gets input from the user and validates it
def getInput():
    
    print("Welcome to Connect 4!\nCode By Noah Hixon\nThis game is for 2 players")
    numOfPlayers = str(input("Do you want the computer to be one player?[y/n]"))
    if numOfPlayers != "y" and numOfPlayers != "n":     # validates computer player input
        validatePlayers(numOfPlayers)
    elif numOfPlayers == "y":
        print("You will play the computer.")
        return "y"
    elif numOfPlayers == "n":
        print("Both players will come from human input.")
        return "n"

# gets the size of the board (number of rows and columns) from the user
def getBoardSize():
    global ROWS # will be global variable
    global COLUMNS # will be global variable
    print("*The default board has 6 rows and 7 columns*")
    
    ROWS = int(input("How many rows would you like? Please enter a number greater than or equal to 5:"))
    while ROWS < 5: # validates ROWS input
        print("You did not enter a valid number.")
        ROWS = int(input("How many rows would you like? Please enter a number greater than or equal to 5:"))
    
    COLUMNS = int(input("How many columns would you like? Please enter a number greater than or equal to 5:"))
    while COLUMNS < 5:  # validates COLUMNS input
        print("You did not enter a valid number")
        COLUMNS = int(input("How many columns would you like? Please enter a number greater than or equal to 5:"))

# creates board and returns it
def createBoard(rows, columns):
    board = []
    for i in range(ROWS):
        temp = []
        for j in range(COLUMNS):
            temp.append("_ ")
        board.append(temp)
    return board


# prints the board in the correct orientation
def printBoard(board,COLUMNS):
    for row in range(len(board)- 1, -1, -1):
        print(board[row], "\n")
        

# checks to see if the user input a valid number for column
def validateColumns(columns):
    while columns > COLUMNS:
        print("That number is not valid")
        columns = int(input("Please choose a column to place your piece(1-" + str(COLUMNS) + "):"))
    return columns


# places the user's piece in the desired column
def dropPiece(board, row, col, piece):
    board[row][col - 1] = piece


# checks the slot the user wants to put a piece and sees if there is a piece already there;
# finds the first empty slot and returns it, if none are empty it returns -1
def slotFull(board, ROWS, column): 
    for row in range(ROWS):
        if board[row][column-1] == "_ ":
            return row
        
    return -1


# checks the board for a winner(4 cases)
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

    
    for col in range(COLUMNS - 3): # this checks diagonally(negative) for win
        for row in range(3, ROWS):
            if board[row][col] == playPiece and board[row - 1][col + 1] == playPiece and board[row - 2][col + 2] and board[row - 3][col + 3]:
                return True

    return False

# main loop for a game with both players coming from human input
def twoPlayer():
    gameWon = False
    turn = 0
    
    board = createBoard(ROWS, COLUMNS)
    printBoard(board, COLUMNS)

    
    while not gameWon:  # while none of the win conditions are met
       
        # player 1 input
        if turn%2 == 0:
            piece = "X"
            print("Player 1, what is your choice?")
            choice = int(input("Choose a column to drop your piece:"))
        
            if choice < 1 or choice > COLUMNS: # validating column choice
                choice = validateColumns(choice)
                
                #row = slotFull(board, ROWS, choice)
                #dropPiece(board, row, choice, piece)
                #printBoard(board, COLUMNS)

            else:
                while slotFull(board, ROWS, choice) == -1:
                    choice = int(input("COLUMN FULL\nEnter a new column:"))
                else:
                    row = slotFull(board, ROWS, choice)
                    dropPiece(board, row, choice, piece)
                    printBoard(board, COLUMNS)
         
            gameWon = checkWin(board, "X")
            turn += 1

        # player 2 input    
        elif turn%2 == 1:
            piece = "O"
            print("Player 2, what is your choice?")
            choice = int(input("Choose a column to drop your piece:"))
            if choice < 1 or choice > COLUMNS:
                choice = validateColumns(choice)
            
            else:
                while slotFull(board, ROWS, choice) == -1:
                    choice = int(input("COLUMN FULL\nEnter a new column:"))
                else:
                    row = slotFull(board, ROWS, choice)
                    dropPiece(board, row, choice, piece)
                    printBoard(board, COLUMNS)
            
            gameWon = checkWin(board, "O")
            turn += 1

    # turn - 1 will be the winner
    if turn%2 == 1:
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")


# main loop for a game versus computer
def computerPlayer():
    gameWon = False
    turn = 0

    board = createBoard(ROWS, COLUMNS)
    printBoard(board, COLUMNS)

    while not gameWon: # while none of the win conditions are met
       
        # player 1 input
        if turn%2 == 0:
            piece = "X"
            print("Player 1, what is your choice?")
            choice = int(input("Choose a column to drop your piece:"))

            if choice < 1 or choice > COLUMNS:
                choice = validateColumns(choice)
            
            else:
                if slotFull(board, ROWS, choice) == -1:
                    choice = int(input("COLUMN FULL\nEnter a new colum:"))
                else:
                    row = slotFull(board, ROWS, choice)
                    dropPiece(board, row, choice, piece)
                    printBoard(board, COLUMNS)
            
            gameWon = checkWin(board, "X")
            turn = turn + 1
            
        # computer input (pseudo-random)    
        else:
            piece = "O"
            compChoice = random.randrange(1, COLUMNS) # the computer's choice is a random number between 1 and amount of columns
            
            
            if slotFull(board, ROWS, compChoice) == -1:
                compChoice = random.randrange(1, COLUMNS)
            else: 
                row = slotFull(board, ROWS, compChoice)
                dropPiece(board, row, compChoice, piece)
                printBoard(board, COLUMNS)
                print("The computer chooses..." + str(compChoice) + "\n" + "------------------------------------" + "\n")
            gameWon = checkWin(board, "O")
            turn += 1
    
    # deciding winner(same as two player)
    if turn % 2 ==1:
        print("Player 1 wins!")
    else:
        print("The computer wins!")
            


# asks the player if they want to play the game again and returns the answer
def playAgain():
    playAgain = input("Do you want to play again? [y/n]")
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Do you want to play again? [y/n]")
    return playAgain

# main game loop
def main():
    
    userInput = getInput() # calls input function
    
    if userInput == "y":
        getBoardSize()
        computerPlayer()

        while playAgain() == "y": 
            userInput = getInput()
            if userInput == "y":
                getBoardSize()
                computerPlayer()
            else:
                getBoardSize()
                twoPlayer()
    
    elif userInput == "n":
        getBoardSize()
        twoPlayer()
        
        while playAgain() == "y":
            userInput = getInput()
            if userInput == "y":
                getBoardSize()
                computerPlayer()
            else:
                getBoardSize()
                twoPlayer()

main()

