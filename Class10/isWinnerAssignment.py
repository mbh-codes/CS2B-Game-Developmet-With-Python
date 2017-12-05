# Here you will create a function that takes in a tic tac toe board and a player's letter as it's parameters and it
# will return a boolean statement. If user wins, returns True. If user doesn't win, returns false.

# Remember a board is a list of ten strings such as the following that consists of ' ', 'X', 'O'
# Also we a skipping board[]
# Ex) board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
# A letter is either 'X' or 'O'

#   789
#   456
#   123
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

# Your code should work with assert statements. If you don't know what assert statements are, don't worry we will
# go over that in class.
# Do not change the code below

assert isWinner([' ','X','X','X','O',' ',' ','O',' ',' '], 'X') == True
assert isWinner([' ','X','O','X','O','X',' ','O',' ','X'], 'X') == True
assert isWinner([' ','X','O','X','O','X',' ','O',' ','X'], 'O') == False
assert isWinner([' ','O','X','X','O',' ',' ','O',' ',' '], 'X') == False
assert isWinner([' ','O','X','X','O',' ',' ','O',' ',' '], 'O') == True

# 1st case
#   O89
#   O56   return false if letter = O
#   XXX   return true if letter = X

# 2nd case
#   O8X
#   OX6 return false if letter is equal to O
#   XOX return true if letter is equal to X

def addtwonumbers(x,y):
    return x + y + 1
assert addtwonumbers(2,3) == 5
