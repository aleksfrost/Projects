class Laptop:

    def __init__(self, brand='None', model='None', price=0):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = self.brand + ' ' + self.model


laptop1 = Laptop('hp', '5464646', 100500)
laptop2 = Laptop()

hp = Laptop('hp', '15-bw0xx', 57000)
print(hp.price) # выводит 57000
print(hp.laptop_name) # выводит "hp 15-bw0xx"