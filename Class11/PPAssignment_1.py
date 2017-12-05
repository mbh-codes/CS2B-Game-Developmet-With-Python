# Getting the Player to make their move

def isSpaceFree(board, move):
    #Returns True if the passed move is free
    return board[move] == ' '

#Complete the following function


# This function will take in a board.
# Then it will ask the player to input an integer that is  between 1-9 inclusively.
# Checks if the move is a valid and is free. For this part you should include the isSpaceFree function
# that we created last class.
# We will return our move which in this case will be represented as an integer.

def getPlayerMove(board):
  move = ''
  while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('What is your move? (1-9)')
        move = input()
  return int(move)
#'h'

#in '1 2 3 4 5 6 7 8 9'.split() #false
