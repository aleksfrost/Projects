import json

specs = {
         'Модель': 'AMD Ryzen 5 5600G',
         'Год релиза': 2021,
         'Сокет': 'AM4',
         'Техпроцесс': '7 нм',
         'Ядро': 'Cezanne',
         'Объем кэша L2': '3 МБ',
         'Объем кэша L3': '16 МБ',
         'Базовая частота': '3900 МГц'
        }
try:
    specs_json = json.dumps(specs, ensure_ascii=False, indent='   ')
except ValueError:
    print('Fu-fu-fu')
    
print(specs_json)