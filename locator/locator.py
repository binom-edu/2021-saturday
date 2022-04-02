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
    while True:
        s = input("Введите номер строки и номер столбца через пробел: ").split()
        if len(s) != 2:
            print('Требуется два значения')
            continue
        if not s[0].isdigit() or not s[1].isdigit():
            print('Введенные значения должны быть целыми числами')
            continue
        i, j = int(s[0]), int(s[1])
        if not (0 <= i < BOARD_HEIGHT and 0 <= j < BOARD_WIDTH):
            print('Координаты должны быть в пределах поля')
            continue
        if not board[i][j] in ALPHA:
            print('Такой ход уже был сделан')
            continue
        return [i, j]

BOARD_WIDTH = 20
BOARD_HEIGHT = 10
MAX_CHESTS = 3
MAX_ATTEMPTS = 30
ALPHA = '~-'

board = getNewBoard()
chests = makeChests()
print(chests)
print(f'Привет. Здесь спрятаны сундуки с сокровищами ({MAX_CHESTS} шт). У вас есть {MAX_ATTEMPTS} попыток, чтобы их отыскать. Используйте локатор!')
for attempt in range(MAX_ATTEMPTS):
    printBoard(board)
    print(f'Осталось попыток: {MAX_ATTEMPTS - attempt}.')
    print(f'Осталось сундуков: {len(chests)}')
    i, j = getUserMove()
    d = locator((i, j))
    if d == 0:
        print('Вы нашли сундук!')
        board[i][j] = '@'
        chests.remove((i, j))
        if len(chests == 0):
            pass
    elif d > 9:
        print('Ничего не найдено')
        board[i][j] = 'X'
    else:
        print('Результат:', d)
        board[i][j] = str(d)