# Encapsulation
# Modify the car class to encapsulate the brand attribute, making it private, and provide a getter method for it
# any variable make private then use double uder score front of this variblename

class Payment:
    def __init__(self, platform, money):
        self.platform = platform
        self.__money = money

    def get_platform(self):
        return "Amount is: " + self.money + ".00 rupee"

    def fulldetails(self):
        return f"{self.platform} {self.__money}"
    
my_payment = Payment("Google Pay", "500")
print(my_payment.platform)
print(my_payment.__money)
print(my_payment.fulldetails())
print(my_payment.get_platform())