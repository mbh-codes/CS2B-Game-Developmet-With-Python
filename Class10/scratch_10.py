def isSpaceFree(board, move):
    #Return True if the passed move is free

    return board[move] == ' '


#[' ','X','X',' ','O',' ',' ','O',' ',' ']

#   O89
#   O56
#   XX3
assert isSpaceFree([' ','X','X',' ','O',' ',' ','O',' ',' '], 3) == True
assert isSpaceFree([' ','X','X','O','O',' ',' ','O',' ',' '], 3) == False
print(isSpaceFree([' ','X','X',' ','O',' ',' ','O',' ',' '], 3))
print(isSpaceFree([' ','X','X','O','O',' ',' ','O',' ',' '], 3))
