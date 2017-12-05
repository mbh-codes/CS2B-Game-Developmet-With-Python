# Choosing a random move from a list of moves
import random
def isSpaceFree(board, move):
    #Returns True if the passed move is free
    return board[move] == ' '

# Complete the following function
# This will take in a board and a movesList
# An example of a movesList value is [1,3,7,9].
# This represents all the corners.
# You will need to first create a list from the moves on the moveList
# that have their space free on the board.
# Hint: Use the isSpaceFree() function

def chooseRandomMoveFromList(board, movesList):
    # Returns a valid move from the passed movesList on the passed board
    # Returns none if there is no valid move
    possibleMoves = []
    for x in movesList:
        if isSpaceFree(board, x):
            possibleMoves.append(x)
    if len(possibleMoves) != 0:
        return random.choice(possibleMoves) #[1,3,7] #9
    else:
        return None
