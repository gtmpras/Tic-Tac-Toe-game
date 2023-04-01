#Simple Tic Tac Toe game project.

import random
# displaying Tic Tac Toe board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
currentPlayer = "X"
winner = None
gameRunning = True


# printing the game board
def printBoard(board):  # storing the positions
    print(board[0] + "|" + board[1]+"|"+board[2])
    print("--------")
    print(board[3] + "|" + board[4]+"|"+board[5])
    print("--------")
    print(board[6] + "|" + board[7]+"|"+board[8])
    print("--------")
# take player input


def playerInput(board):
    # Accepting numbers as positions
    inp = int(input("Enter the number 1-9: "))
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
        board[inp-1] = currentPlayer
    else:
        print("Player is already in the spot")


# check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#computer  for auto player as "O"
def computerauto():
    while currentPlayer=="O":
        position = random.randint(0,8)
        if board[position]=="-":
            board[position]="O"
            switchPlayer()
    

def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    if board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    if board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("It's a tie!")
        gameRunning = False


def checkWin():
    if checkDiagonal(board) or checkHorizontal(board) or checkRow(board):
        print(f"The winner is {winner}")


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":  # boolean expression checking if currentplayer at moment is X so, assign player with O
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# check for win or tie again
while gameRunning:
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computerauto()
    checkWin()
    checkTie(board)
