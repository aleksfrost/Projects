class LengthError(Exception):
    pass


class LetterError(Exception):
    pass


class DigitError(Exception):
    pass


def is_good_password(string: str) -> bool:
    try:
        if len(string) < 9:
            raise LengthError
        if string.lower() == string or string.upper() == string:
            raise LetterError
        if not any([x.isdigit() for x in string]):
            raise DigitError
    except (LengthError, LetterError, DigitError):
        return False
    else:
        return True


try:
    print(is_good_password('Short7'))
except Exception as err:
    print(type(err))

print(is_good_password('еПQSНгиfУЙ70qE'))

try:
    print(is_good_password('41157081231232'))
except Exception as err:
    print(type(err))