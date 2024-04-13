# basic_class_and_object
# create a Car class with attributes like brand and model. 
# Then create an instance of this class.
# there self and in java this keyword same

class Car:
    def __init__(self, brand, model): # ehape init likhunga to hum Car() k under parameter de sakte hain
        self.brand = brand
        self.model = model
my_car = Car("Lmborgini", "New") # this Car and upar class bala Car connect karne keliye self keyword likhte hain
print(my_car.brand,my_car.model)
