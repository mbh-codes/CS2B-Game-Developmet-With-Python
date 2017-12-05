# November 18, 2017
# Tic Tac Toe

import random

def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
def inputPlayerLetter():
    #Lets the player enter which letter they want to play with
    #Returns a list with the player's letter as the first item and the computer's letter as the second.
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    #The first element in the list is the player's letter; the second is the computer's
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    #Randomly choose which player goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    #Takes in a board and a letter.
    # Returns true if letter wins.
    return((board[7] == letter and board[8] == letter and board[9] == letter) or
           (board[4] == letter and board[5] == letter and board [6] == letter) or
           (board[1] == letter and board[2] == letter and board [3] == letter) or
           (board[7] == letter and board[4] == letter and board [1] == letter) or
           (board[8] == letter and board[5] == letter and board [2] == letter) or
           (board[9] == letter and board[6] == letter and board [3] == letter) or
           (board[7] == letter and board[5] == letter and board [3] == letter) or
           (board[1] == letter and board[5] == letter and board [9] == letter))

def getBoardCopy(board):
    #This returns a copy of the board.
    #This allows the computer to test
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    #Returns True if the passed move is free
    return board[move] == ' '
