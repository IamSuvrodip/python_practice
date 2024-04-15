# timing_function
# Write a decorator that measures the time a funtion takes to execute

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name_z_} ran in {end - start} time")
        return result
    return wrapper

def example_functon():
    