# Creating the Computer AI
def makeMove(board, letter, move):
    board[move] = letter
def isWinner(board, letter):
    #Enter code in here
    return((board[7] == letter and board[8] == letter and board[9] == letter) or
           (board[4] == letter and board[5] == letter and board [6] == letter) or
           (board[1] == letter and board[2] == letter and board [3] == letter) or
           (board[7] == letter and board[4] == letter and board [1] == letter) or
           (board[8] == letter and board[5] == letter and board [2] == letter) or
           (board[9] == letter and board[6] == letter and board [3] == letter) or
           (board[7] == letter and board[5] == letter and board [3] == letter) or
           (board[1] == letter and board[5] == letter and board [9] == letter))
def getBoardCopy(board):
    #this makes a copy of the board
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    #Returns True if the passed move is free
    return board[move] == ' '

# This will be  a lengthy assignment and this will involve some time to think about.
#1. See if there’s a move the computer can make that will win the game. If
# there is, take that move. Otherwise, go to step 2.
#2. See if there’s a move the player can make that will cause the computer
#to lose the game. If there is, the computer should move there to block
# the player. Otherwise, go to step 3.
#3. Check if any of the corners (spaces 1, 3, 7, or 9) are free. If no corner
# space is free, go to step 4.
#4. Check if the center is free. If so, move there. If it isn’t, go to step 5.
#5. Move on any of the sides (spaces 2, 4, 6, or 8). There are no more steps,
# because the side spaces are the only spaces left if the execution has
# reached this step.

def getComputerMove(board, computerLetter):
    # Given a board and the computer's letter, determine where to move
    # and return that move.
    playerLetter = ''
    if computerLetter == 'X':
        playerLetter == 'O'
    else:
        playerLetter == 'X'
    # Here is the algorithm for our Tic-Tac-Toe AI:
    # First, check if we can win in the next move.
    for i in range(1, 10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
    # We will now have to check if we can block the player from winning.
    return
