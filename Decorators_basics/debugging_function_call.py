# debugging_function_call
# create a decorator to print the function name 
# and the values of its argumants every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        a
        return func(*args, **kwargs)
    
        
    return wrapper









def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}")

greet("Suvrodip", greeting= "Hi...")#------>replace hello to Hi....