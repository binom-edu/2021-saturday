import random

def getNewBoard() -> list:
    board = []
    for i in range(BOARD_HEIGHT):
        buf = []
        for j in range(BAORD_WIDTH):
            buf.append(random.choice(ALPHA))
        board.append(buf)
    return board

def printBoard(board: list):
    # выводим номера столбцов
    for x in range(BAORD_WIDTH):
        print(x // 10, end='')
    print()
    for x in range(BAORD_WIDTH):
        print(x % 10, end='')
    print()
    # выводим строки
    for y in range(BOARD_HEIGHT):
        print(y, '|', ''.join(board[y]), sep='')
    
BAORD_WIDTH = 40
BOARD_HEIGHT = 15
MAX_CHESTS = 3
MAX_ATTEMPTS = 30
ALPHA = '~-'

board = getNewBoard()
printBoard(board)