import random

NUM_DIGITS = 3
MAX_ATTEMPTS = 20

# создаем строку - загаданное число без повторяющихся цифр
def generateSecret():
    digits = '0 1 2 3 4 5 6 7 8 9'.split()
    random.shuffle(digits)
    result = digits[:NUM_DIGITS]
    return ''.join(result)

# проверяем ответ пользователя
def check(secret: str, userChoice: str) -> dict:
    res = {'bulls': 0, 'cows': 0}   
    # это словарь. Он похож на список, но у его элементов не номера, а имена.
    for i in range(NUM_DIGITS):
        if secret[i] == userChoice[i]:
            res['bulls'] += 1
        elif userChoice[i] in secret:
            res['cows'] += 1
    return res

# получаем ход пользователя
def getUserMove() -> str:
    while True:
        s = input('Введите число: ')
        if len(s) != NUM_DIGITS:
            print(f'Требуется ровно {NUM_DIGITS} символов.')
            continue
        if not s.isdigit():
            print('Недопустимые символы')
            continue
        return s

print('Быки и коровы')
print(f'Привет. Загадано число из {NUM_DIGITS} символов. У вас есть {MAX_ATTEMPTS} попыток, чтобы отгадать его. После каждой попытки вы получите подсказку: Быки - если угадана и цифра, и ее позиция. Коровы - угадана только цифра, но не ее позиция')
secret = generateSecret()
for i in range(MAX_ATTEMPTS):
    print('Попытка номер', i + 1)
    userChoice = getUserMove()
    result = check(secret, userChoice)
    print('Быки:', result['bulls'], ', коровы:', result['cows'])
    if result['bulls'] == NUM_DIGITS:
        print('Вы выиграли. Использовано попыток:', i + 1)
        break
else:
    print('Попытки закончились. Было загадано число', secret)