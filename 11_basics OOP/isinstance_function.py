# class inheritance and isinstance() function
# Demostrate the use of isinstance() to check if my_tesla is an instance
# and Car and ElectricCar

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

my_tesla = ElectricCar("Tesla", " Model:-S", "85KWH")

print(isinstance(my_tesla, Car))
print(isinstance(my_tesla, ElectricCar))


# print(my_tesla.fullname())
# print(my_tesla.brand,my_tesla.model,my_tesla.battery_size,'\n')

# my_car = Car("Lamborgini", "Urus")
# print(my_car.fullname())
# print(my_car.brand,my_car.model)
