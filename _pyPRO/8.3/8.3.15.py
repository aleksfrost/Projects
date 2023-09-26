def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True
    elif word[len(word) - 1] != word[0]:
        return False
    else:
        return is_palindrome(word[1:len(word)-1])


print(is_palindrome('stepik'))
print(is_palindrome('level'))
print(is_palindrome('122333221'))
print(is_palindrome('3'))
print(is_palindrome(''))
