# functions with **kwargs
# beat for database

def print_kwargs(**kwargs):
    #print("Name", name, "Address", address)#------>X
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_kwargs(name="Suvrodip", address="Basirhat")
print_kwargs(name="Suvrodip")
print_kwargs(address="Basirhat", phone=3543459)
