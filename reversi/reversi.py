def getNewBoard() -> list:
    board = []
    for i in range(8):
        buf = [EMPTY] * 8
        board.append(buf)
    board[3][3] = TILES[0]
    board[4][4] = TILES[0]
    board[3][4] = TILES[1]
    board[4][3] = TILES[1]
    return board

def printBoard(board):
    print('  a b c d e f g h')
    for i in range(8):
        print(8 - i, ' '.join(board[i]), 8 - i)
    print('  a b c d e f g h')

def selectUserTile() -> list:
    userTile, computerTile = TILES
    print('Вы играете за ', userTile, '. Поменять (y/n)?', sep='')
    if input().lower().startswith('y'):
        userTile, computerTile = computerTile, userTile
    return [userTile, computerTile]

def tilesToFlip(board: list, y: int, x: int, tile: str) -> list:
    ans = []
    otherTile = ... # определить вражескую фишку
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1]
        [-1, -1]
    ]
    for di, dj in directions:
        i, j = y, x
        while True:
            i += di
            j += dj
            # выход за край доски
            if i < 0:
                break

TILES = ['●', '○']
EMPTY = '·'

board = getNewBoard()
printBoard(board)
userTile, computerTile = selectUserTile()