# property_decorators
# Use a property decorator in the Car class 
# to make the model attribute read-only

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model # make it private and only read not changeable
    
    def fullname(self):
        return f"{self.brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @property #------->this is decorator
    def model(self):
        return self.__model

my_car = Car("Lamborgini", "Urus")
# my_car.model = "Aventador" #------->not changed
# print(my_car.model()) #-------->'str' object is not callable
print(my_car.model)
print(my_car.fullname())