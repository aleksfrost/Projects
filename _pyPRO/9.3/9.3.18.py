import string


def verification(login, password, success, failure):
    if any(map(lambda x: x in string.ascii_letters, password)):
        if any(map(lambda x: x in string.ascii_uppercase, password)):
            if any(map(lambda x: x in string.ascii_lowercase, password)):
                if any(map(lambda x: x in string.digits, password)):
                    success(login)
                else:
                    failure(login, "в пароле нет ни одной цифры")
            else:
                failure(login, "в пароле нет ни одной строчной буквы")
        else:
            failure(login, "в пароле нет ни одной заглавной буквы")
    else:
        failure(login, "в пароле нет ни одной буквы")


def success(login):
    print(f'Привет, {login}!')


def failure(login, text):
    print(f'{login}, попробуйте снова. Ошибка: {text}')

verification('timyrik20', 'Beegeek314', success, failure)


def success(login):
    print(f'Здравствуйте, {login}!')

def failure(login, text):
    print(f'{login}, попробуйте снова. Текст ошибки: {text}')

verification('Ruslan_Chaniev', 'stepikstepik2', success, failure)
