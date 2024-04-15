# debugging_function_call
# create a decorator to print the function name 
# and the values of its argumants every time the function is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)#-------give iterable list
        kwargs_value = ', '.join(f"{k} = {v}"for k, v in kwargs.items())
        print(f"calling:function name= ({func.__name__}) with args= ({args_value}) and kwargs= ({kwargs_value})")

        return func(*args, **kwargs)  
    return wrapper


@debug
def hello():
    print("Hi.. Rudro\n")


@debug
def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}")

hello()
greet("Suvrodip", greeting= "Hi...")#------>replace hello to Hi....