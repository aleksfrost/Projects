class Vehicle:

    def __init__(self, max_speed=0, mileage=0):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle(240, 18)
print(modelX.max_speed, modelX.mileage)# 240 18
