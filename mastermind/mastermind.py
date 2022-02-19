import random

NUM_DIGITS = 3
MAX_ATTEMPTS = 20

# создаем строку - загаданное число без повторяющихся цифр
def generateSecret():
    digits = '0 1 2 3 4 5 6 7 8 9'.split()
    random.shuffle(digits)
    result = digits[:NUM_DIGITS]
    return ''.join(result)

print(generateSecret())