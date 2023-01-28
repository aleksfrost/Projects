import random

word_list = ['banana', 'transgression', 'dinosaur', 'ringtone', 'ball', 'refrigeratora']
again = 'yes'

def get_word():
    res = random.choice(word_list)
    return res.upper()


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)

    while not guessed:
        temp = input('Угадай букву или слово: ').upper()
        tries -= 1
        if temp.encode().isalpha():
            if len(temp) == 1 and temp not in guessed_letters:
                if temp in guessed_letters:
                    tries += 1
                    print('Уже называлось, попробуй еще:')
                if temp in word:
                    for i in range(len(word)):
                        if temp == word[i]:
                            word_completion = word_completion[:i] + temp + word_completion[i + 1:]
                    if '_' not in word_completion:
                        print('Поздравляем, вы угадали слово! Вы победили!')
                        print(f'Загаданное слово: {word}')
                        break
                else:
                    guessed_letters.append(temp)
                    print('Нет такой')
            if len(temp) > 1:
                if temp == word:
                    guessed = True
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    print(f'Загаданное слово: {word}')
                else:
                    if temp in guessed_words:
                        print('Было уже. Попробуй еще')
                        tries += 1
                    else:
                        guessed_words.append(temp)
                        print('Не угадал. Еще раз букву или слово')
        else:
            tries += 1
            print('Не верный ввод. Только буквы или слово:')
        if not guessed:
            print(display_hangman(tries))
            print(word_completion)
            print(f'Осталось {tries} попыток')
        if tries == 0:
            print(f'Попытки кончились. Загаданное слово: {word}')
            break




while again == 'yes':
    play(get_word())
    again = input('Еще раз? (yes/no)')


# Улучшения проекта
# Можно отображать первую и последнюю букву слова;
# Слова можно выделить в категории и давать подсказку пользователю;
# Существует также вариант игры с 8 частями — добавляются ступни, а также самый длинный вариант, когда сначала за не отгаданную букву рисуются части самой виселицы.