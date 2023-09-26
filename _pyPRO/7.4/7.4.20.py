import json

try:
    with open(input(), encoding='utf-8') as file:
        try:
            data = json.load(file)
            print(data)
        except json.decoder.JSONDecodeError:
            print('Ошибка при десериализации')
except FileNotFoundError:
    print('Файл не найден')

