print("-----A simple Tic-Tac-Toe game!-----")
print()
gameRun = True
board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
playerX = input('Who is playing X? ')
playerO = input('Who is playing O? ')
turns = [0, 1, 2, 3, 4, 5, 6, 7, 8]
usedSpot = [0, 1, 2, 3, 4, 5, 6, 7, 8]
n = 1


def displayBoard():
    print(f'[{board[0]}] [{board[1]}] [{board[2]}]')
    print(f'[{board[3]}] [{board[4]}] [{board[5]}]')
    print(f'[{board[6]}] [{board[7]}] [{board[8]}]')

# play game
def playGame():
    global gameRun
    while gameRun:
        playerTurn()
        checkColumn()
        checkRow()
        checkDiagonal()
        checkWin()
        checkTie()

def playerTurn():
    global n
    if n % 2 != 0:
        displayBoard()
        turnChoice = boardPlace(playerX)
        board[turnChoice] = 'X'
    else:
        displayBoard()
        turnChoice = boardPlace(playerO)
        board[turnChoice] = 'O'
    n += 1

def boardPlace(player):
    turnChoice = int(input(f"{player}, make your move. "))
    turnChoice = turnChoice - 1
    while turnChoice not in turns:
        turnChoice = int(input(f"{player}, make your move. "))
        turnChoice = turnChoice - 1
    while turnChoice not in usedSpot:
        turnChoice = int(input("Already taken. Make another move. "))
        turnChoice = turnChoice - 1 
        while turnChoice not in turns:
            turnChoice = int(input(f"{player}, make your move. "))
            turnChoice = turnChoice - 1
    usedSpot.remove(turnChoice)
    return turnChoice

def checkRow():
    global gameRun
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'
    if row1 or row2 or row3:
        gameRun = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]

def checkColumn():
    global gameRun
    column1 = board[0] == board[3] == board[6] != '-'
    column2 = board[1] == board[4] == board[7] != '-'
    column3 = board[2] == board[5] == board[8] != '-'
    if column1 or column2 or column3:
        gameRun = False

    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]

def checkDiagonal():
    global gameRun
    diagonal1 = board[0] == board[4] == board[8] != '-'
    diagonal2 = board[2] == board[4] == board[6] != '-'
    if diagonal1 or diagonal2:
        gameRun = False

    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]

def checkWin():
    if checkColumn() == 'X':
        displayBoard()
        print(f"{playerX} won.")
    elif checkColumn() == 'O':
        displayBoard()
        print(f"{playerO} won.")
    elif checkRow() == 'X':
        displayBoard()
        print(f"{playerX} won.")
    elif checkRow() == 'O':
        displayBoard()
        print(f"{playerO} won.")
    elif checkDiagonal() == 'X':
        displayBoard()
        print(f"{playerX} won.")
    elif checkDiagonal() == 'O':
        displayBoard()
        print(f"{playerO} won.")

def checkTie():
    global gameRun
    if '-' not in board:
        displayBoard()
        print("It's a tie!")
        gameRun = False
if __name__ == "__main__":
    playGame()