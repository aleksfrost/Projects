import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):

    def say_hello(self):
        return 'LengthError'


class LetterError(PasswordError):

    def say_hello(self):
        return 'LetterError'


class DigitError(PasswordError):

    def say_hello(self):
        return 'DigitError'


def is_good_password(string: str) -> bool:
    try:
        if len(string) < 9:
            raise LengthError
        if string.lower() == string or string.upper() == string:
            raise LetterError
        if not any([x.isdigit() for x in string]):
            raise DigitError
    except (LengthError, LetterError, DigitError) as e:
        print(e.say_hello())
    else:
        print('Success!')
        return True


reader = sys.stdin
is_success = False
while not is_success:
    if is_good_password(reader.readline().strip()):
        is_success = False
        reader.close()
        break



