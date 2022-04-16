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
        print(8 - i, ' '.join(board[i]))

def selectUserTile() -> list:
    pass
# написать функцию для выбора игроком своих фишек


TILES = ['●', '○']
EMPTY = '·'

board = getNewBoard()
printBoard(board)
userTile, computerTile = selectUserTile()