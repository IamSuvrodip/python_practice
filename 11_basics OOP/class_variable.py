# class_variable

# Add class variable to Car 
# That keeps track of the number of cars created

# polymorphism

# Demostrate polymorphism by 
# defining a method fuel_type in both Car and ElectricCar classes
# but with different behaviors

class Car:
    total_car = 0
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car += 1
        Car.total_car += 1
    
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
my_car = Car("Tata", "Safari")
my_car2 = Car("Lambo", "Urus")
print(my_Ecar.fullname())
print(my_Ecar.brand,my_Ecar.model,my_Ecar.battery_size)
print(my_Ecar.fuel_type(),'\n')

print(my_car.fuel_type(),'\n')

print(my_car2.fullname(),'\n')

print("Total car is:",Car.total_car,"\n")




