# multiple_inheritance

# Create two class Battery and Engine,
# and let the ElectricCar class inherit from both,
# demostrating

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"

class Battery:
    def battery_info(self):
        return "this is Battery"
class Engine:
    def engine_info(self):
        return "this is Engine"
    
class ElectricCar(Car, Battery, Engine): #-----------> ElectricCar inherits all properties of Car,Battery,Engine
    pass

my_tesla = ElectricCar("Tesla", " Model:-S")
print(my_tesla.fullname())
print(my_tesla.battery_info())
print(my_tesla.engine_info())




