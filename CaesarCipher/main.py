# Примечание 1. Считайте, что в русском языке 32 буквы (буква ё отсутствует).
# Примечание 2. Неалфавитные символы — знаки препинания, пробелы, цифры — не меняются.
# А-Я - 1040 - 1071
# а-я - 1072 - 1103
# A-Z - 0041 - 0066



# way = input('Введи направление шифрования (шифр - e/дешифр - d )')
# language = input('Выбери язык (en/ru): ')
# step = input('Введи шаг: ')

way = 'd'
language = 'en'
# stepp = 25
# text_ru = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
text_en = 'Hawnj pk swhg xabkna ukq nqj.'


def ru_encode(text, step):
    text_coded_ru = ''
    for ch in text:
        if ch.isupper():
            if (ord(ch) + step) > ord('Я'):
                text_coded_ru += chr(ord(ch) - 31 + step)
            else:
                text_coded_ru += chr(ord(ch) + step)
        elif ch.islower():
            if (ord(ch.upper()) + step) > ord('Я'):
                text_coded_ru += chr(ord(ch.upper()) - 31 + step).lower()
            else:
                text_coded_ru += chr(ord(ch.upper()) + step).lower()
        else:
            text_coded_ru += ch
    return text_coded_ru


def ru_decode(text, step):
    text_coded_ru = ''
    alphabet_ru_up = [chr(c) for c in range(ord('А'), ord('Я') + 1)]
    alphabet_ru_low = [chr(c) for c in range(ord('а'), ord('я') + 1)]
    for ch in text:
        if ch.isupper():
            if alphabet_ru_up.index(ch) + step < 0:
                text_coded_ru += alphabet_ru_up[alphabet_ru_up.index(ch) + 32 - step]
            else:
                text_coded_ru += alphabet_ru_up[alphabet_ru_up.index(ch) - step]
        elif ch.islower():
            if alphabet_ru_low.index(ch) + step < 0:
                text_coded_ru += alphabet_ru_low[alphabet_ru_low.index(ch) + 32 - step]
            else:
                text_coded_ru += alphabet_ru_low[alphabet_ru_low.index(ch) - step]
        else:
            text_coded_ru += ch
    return text_coded_ru


def en_encode(text, step):
    text_coded_en = ''
    alphabet_eng_up = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    alphabet_eng_low = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    for ch in text:
        if ch.isupper():
            if alphabet_eng_up.index(ch) + step > len(alphabet_eng_up):
                text_coded_en += alphabet_eng_up[alphabet_eng_up.index(ch) - 26 + step]
            else:
                text_coded_en += alphabet_eng_up[alphabet_eng_up.index(ch) + step]
        elif ch.islower():
            if alphabet_eng_low.index(ch) + step > len(alphabet_eng_low):
                text_coded_en += alphabet_eng_low[alphabet_eng_low.index(ch) - 26 + step]
            else:
                text_coded_en += alphabet_eng_low[alphabet_eng_low.index(ch) + step]
        else:
            text_coded_en += ch
    return text_coded_en


def en_decode(text, step):
    text_coded_en = ''
    alphabet_eng_up = [chr(c) for c in range(ord('A'), ord('Z') + 1)]
    alphabet_eng_low = [chr(c) for c in range(ord('a'), ord('z') + 1)]
    for ch in text:
        if ch.isupper():
            if alphabet_eng_up.index(ch) + step < 0:
                text_coded_en += alphabet_eng_up[alphabet_eng_up.index(ch) + 26 - step]
            else:
                text_coded_en += alphabet_eng_up[alphabet_eng_up.index(ch) - step]
        elif ch.islower():
            if alphabet_eng_low.index(ch) + step < 0:
                text_coded_en += alphabet_eng_low[alphabet_eng_low.index(ch) + 26 - step]
            else:
                text_coded_en += alphabet_eng_low[alphabet_eng_low.index(ch) - step]
        else:
            text_coded_en += ch
    return text_coded_en


# if language == 'ru' and way == 'e':
#     print(ru_encode(text_ru, stepp))
# if language == 'en' and way == 'e':
#     print(en_encode(text_en, stepp))
# if language == 'ru' and way == 'd':
#     print(ru_decode(text_ru, stepp))
# if language == 'en' and way == 'd':
#     print(en_decode(text_en, stepp))
stepp = 0
for _ in range (1, 26):
    stepp += 1
    if language == 'en' and way == 'd':
        print(en_decode(text_en, stepp))

