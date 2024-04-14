# static_method
# Add a static method to the Car class thet returns a general description of a car.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    # static method
    @staticmethod
    def general_description(): #------>not to need slef
        return "Super Car"


my_car = Car("Lamborgini", "Urus")
print(my_car.fuel_type())
print(my_car.general_description())





'''
@staticmethod
def general_description():
        return "Super Car"

my_car = Car("Lamborgini", "Urus")
print(my_car.general_description())'''




'''def general_description(self):
        return "Super Car"

my_car = Car("Lamborgini", "Urus")
print(my_car.general_description())'''




'''def general_description():
        return "Super Car"

my_car = Car("Lamborgini", "Urus")
print(Car.general_description())'''

