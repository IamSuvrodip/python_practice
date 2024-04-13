# Method and Self
# Add a method to the Car class thet displays the full name of the car(brand and model)

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def fullname(self):
        return f"{self.brand} {self.model}"



my_car = Car("Lmborgini", "New")
print(my_car.brand)
print(my_car.fullname())