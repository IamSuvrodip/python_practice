# inheritance
# create a ElectricCar class that inherits from the Car class and has an additional attribute battery size

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car): #-----------> ElectricCar inherits all properties of Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

my_car = ElectricCar("Tesla", " Model:-S", "85KWH")
print(my_car.fullname())
print(my_car.brand,my_car.model,my_car.battery_size)
