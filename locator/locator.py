import random

def getNewBoard() -> list:
    board = []
    for i in range(BOARD_HEIGHT):
        buf = []
        for j in range(BOARD_WIDTH):
            buf.append(random.choice(ALPHA))
        board.append(buf)
    return board

def printBoard(board: list):
    # выводим номера столбцов
    print('   ', end='')
    for x in range(BOARD_WIDTH):
        print(x // 10, end='')
    print()
    print('   ', end='')
    for x in range(BOARD_WIDTH):
        print(x % 10, end='')
    print()
    # выводим строки
    for y in range(BOARD_HEIGHT):
        print('%2d' % (y), '|', ''.join(board[y]), sep='')
    
def makeChests():
    chests = []
    while len(chests) < MAX_CHESTS:
        x = random.randint(0, BOARD_WIDTH - 1)
        y = random.randint(0, BOARD_HEIGHT - 1)
        if (y, x) not in chests:
            chests.append((y, x))
    return chests

def distance(a: tuple, b: tuple) -> float:
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def locator(coords: tuple) -> int:
    ans = 10
    for chest in chests:
        d = int(distance(coords, chest))
        if d < ans:
            ans = d
    return d

def getUserMove():
    pass

BOARD_WIDTH = 40
BOARD_HEIGHT = 15
MAX_CHESTS = 3
MAX_ATTEMPTS = 30
ALPHA = '~-'

board = getNewBoard()
printBoard(board)
chests = makeChests()
print(chests)