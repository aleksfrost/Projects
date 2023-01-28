class CustomLabel:

    def __init__(self, text, **kwargs):
        self.text = text
        if kwargs:
            for item in kwargs.items():
                self.__setattr__(item[0], item[1])

    def config(self, **kwargs):
        if kwargs:
            for item in kwargs.items():
                self.__setattr__(item[0], item[1])


label = CustomLabel(text="Hello", bd=20, bg='#ffaaaa')

print(label.__dict__) # {'text': 'Hello', 'bd': 20, 'bg': '#ffaaaa'}

label.config(color='red', bd=100)

print(label.__dict__) # {'text': 'Hello', 'bd': 100, 'bg': '#ffaaaa', 'color': 'red'}