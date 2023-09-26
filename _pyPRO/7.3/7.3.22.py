
try:
    with open(input(), encoding='utf-8') as file:
        text = file.read()
        print(text)
except FileNotFoundError:
    print('Файл не найден')
