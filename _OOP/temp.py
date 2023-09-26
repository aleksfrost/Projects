import time
from datetime import datetime


class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print(f"К атрибуту _name обращались в {datetime.now()}")
        return self._name

    def set_name(self, new_name):
        print(f"Атрибут _name изменился в {datetime.now()}")
        self._name = new_name


bob = Person('bob')
print(bob.get_name())
time.sleep(3)
bob.set_name('Bill')
print(bob.get_name())