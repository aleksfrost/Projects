class Alphabet:
    def __init__(self, language):
        self.language = language
        self.en = 'abcdefghijklmnopqrstuvwxyz'
        self.ru = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.en_len = len(self.en)
        self.ru_len = len(self.ru)
        self.start = 0


    def __iter__(self):
        return self

    def __next__(self):
        if self.language == 'en':
            self.res = self.en[self.start]
            self.it_len = self.en_len
        if self.language == 'ru':
            self.res = self.ru[self.start]
            self.it_len = self.ru_len
        self.start += 1
        if self.start == self.it_len:
            self.start = 0
        return self.res


ru_alpha = Alphabet('ru')

print(next(ru_alpha))
print(next(ru_alpha))
print(next(ru_alpha))


en_alpha = Alphabet('en')

letters = [next(en_alpha) for _ in range(28)]

print(*letters)
