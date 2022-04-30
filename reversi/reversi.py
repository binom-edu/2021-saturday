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
    p = TILES.index(tile)
    otherTile = TILES[(p + 1) % 2] # вражеская фишка
    directions = [
        [-1, 0],
        [-1, 1],
        [0, 1],
        [1, 1],
        [1, 0],
        [1, -1],
        [0, -1],
        [-1, -1]
    ]
    for di, dj in directions:
        i, j = y, x
        while True:
            i += di
            j += dj
            # выход за край доски
            if i < 0 or i > 7 or j < 0 or j > 7:
                break
            # пустая клетка
            if board[i][j] == EMPTY:
                break
            # вражеская фишка
            if board[i][j] == otherTile:
                continue
            # своя фишка
            if board[i][j] == tile:
                i -= di
                j -= dj
                while not (i == y and j == x):
                    ans.append([i, j])
                    i -= di
                    j -= dj
                break
    return ans

def getUserMove(board: list):
    # получить ход игрока
    pass

TILES = ['●', '○']
EMPTY = '·'

board = getNewBoard()
printBoard(board)
userTile, computerTile = selectUserTile()
print(tilesToFlip(board, 4, 2, TILES[0]))