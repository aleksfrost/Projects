class Library:
    def __init__(self, books: list):
        self.__books = books

    def __check_availability(self, book):
        if book in self.__books:
            return True
        else:
            return False

    def search_book(self, book):
        return self.__check_availability(book)

    def return_book(self, book):
        self.__books.append(book)

    def _checkout_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            return True
        else:
            return False
