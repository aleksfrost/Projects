# pop() by default is -1. so + or append

class Stack:

    def __init__(self):
        self.values = list()

    def push(self, item):
        self.values.insert(0, item)

    def pop(self):
        try:
            return self.values.pop(0)
        except IndexError:
            print('Empty Stack')

    def peek(self):
        try:
            return self.values[0]
        except IndexError:
            print('Empty Stack')
            return None

    def is_empty(self):
        if len(self.values):
            return False
        else:
            return True

    def size(self):
        return len(self.values)


s = Stack()
s.peek()  # распечатает 'Empty Stack'
print(s.is_empty())  # распечатает True
s.push('cat')  # кладем элемент 'cat' на вершину стека
s.push('dog')  # кладем элемент 'dog' на вершину стека
print(s.peek())  # распечатает 'dog'
s.push(True)  # кладем элемент True на вершину стека
print(s.size())  # распечатает 3
print(s.is_empty())  # распечатает False
s.push(777)  # кладем элемент 777 на вершину стека
print(s.pop())  # удаляем элемент 777 с вершины стека и печатаем его
print(s.pop())  # удаляем элемент True с вершины стека и печатаем его
print(s.size())  # распечатает 2