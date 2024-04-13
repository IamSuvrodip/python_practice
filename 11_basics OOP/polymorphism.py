# polymorphism

# Demostrate polymorphism by 
# defining a method fuel_type in both Car and ElectricCar classes
# but with different behaviors

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"

class ElectricCar(Car): #-----------> ElectricCar inherits all properties of Car
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size

    def fuel_type(self):
        return "Electric Charge"

my_Ecar = ElectricCar("Tesla", " Model:-S", "85KWH")
print(my_Ecar.fullname())
print(my_Ecar.brand,my_Ecar.model,my_Ecar.battery_size)
print(my_Ecar.fuel_type(),'\n')

my_car = Car("Tata", "Safari")
print(my_car.fuel_type())

