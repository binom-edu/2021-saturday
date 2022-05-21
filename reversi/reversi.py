import random

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
    score = getScore(board)
    print(f"Пользователь: {userTile}{score['user']}, Компьютер: {computerTile}{score['computer']}")
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

def makeMove(board: list, y: int, x: int, tile: str):
    for i, j in tilesToFlip(board, y, x, tile):
        board[i][j] = tile
    board[y][x] = tile

def getValidMoves(board: list, tile: str) -> list:
    result = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == EMPTY and len(tilesToFlip(board, i, j, tile)) > 0:
                result.append([i, j])
    return result

def getComputerMove(board: list):
    i, j = random.choice(getValidMoves(board, computerTile))
    print(f"Ход компьютера: {'abcdefgh'[j]}{8-i}")
    makeMove(board, i, j, computerTile)

def getScore(board: list):
    score = {'user': 0, 'computer': 0}
    for i in range(8):
        for j in range(8):
            if board[i][j] == userTile:
                score['user'] += 1
            elif board[i][j] == computerTile:
                score['computer'] += 1
    return score

def getUserMove(board: list):
    while True:
        s = input('Ваш ход: ')
        if len(s) != 2:
            print('Некорректный ввод')
            continue
        alf = 'abcdefgh'
        digits = '12345678'
        if not s[0].lower() in alf or not s[1] in digits:
            print('Некорректный ввод')
            continue
        i = 8 - int(s[1])
        j = alf.find(s[0].lower())
        if board[i][j] != EMPTY:
            print('Эта клетка уже занята')
            continue
        if len(tilesToFlip(board, i, j, userTile)) == 0:
            print('Нет окруженных фишек')
            continue
        makeMove(board, i, j, userTile)
        return

TILES = ['●', '○']
EMPTY = '·'

userTile, computerTile = TILES
board = getNewBoard()
printBoard(board)
userTile, computerTile = selectUserTile()

gameOn = True
while gameOn:
    if getValidMoves(board, userTile):
        getUserMove(board)
        printBoard(board)
    if getValidMoves(board, computerTile):
        getComputerMove(board)
        printBoard(board)
    if not (getValidMoves(board, userTile) or getValidMoves(board, computerTile)):
        gameOn = False

print('Игра окончена')
score = getScore(board)
if score['user'] > score['computer']:
    print('Вы победили')
elif score['user'] < score['computer']:
    print('Вы проиграли')
else:
    print('Ничья')