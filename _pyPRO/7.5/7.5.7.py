def is_good_password(string: str) -> bool:
    if isinstance(string, str) and len(string) > 8:
        if string.lower() != string and string.upper() != string:
            if any([x.isdigit() for x in string]):
                return True
        return False
    return False


print(is_good_password('41157082'))
print(is_good_password('мойпарольсамыйлучший'))
print(is_good_password('МойПарольСамыйЛучший111'))
