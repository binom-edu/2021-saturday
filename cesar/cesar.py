def encrypt(s: str, key: int, decrypt=False) -> str:
    res = ''
    if decrypt:
        key = -key
    for i in s:
        if i in ALF:
            pos = ALF.find(i)
            res += ALF[(pos + key) % len(ALF)]
        else:
            res += i
    return res

def decrypt(s: str, key: int) -> str:
    return encrypt(s, -key)

ALF = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'

s = input('Введите текст: ')
key = int(input('Укажите ключ: '))
task = input('Шифровать - 1, дешифровать - 2: ')
if task == '1':
    res = encrypt(s, key)
else:
    res = encrypt(s, key, decrypt=True)
print(res)