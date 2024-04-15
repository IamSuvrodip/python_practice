# timing_function
# Write a decorator that measures the time a funtion takes to execute

#timer ko tol banana hain matlab koibi functions ischee hokei gujre to decorate kardo us function ko (@timer matlab kisse gujarna hain)

#func.__name__ for ptint function name

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end - start} time") #-------->formated string
        return result
    return wrapper

@timer
def example_functon(n):
    time.sleep(n)

example_functon(3)

    