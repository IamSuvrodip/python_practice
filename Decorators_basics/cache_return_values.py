# vcache_return_values
# Implement a decorator that caches the return values of a function, 
# so that when it's called with the same arguments, 
# the cached value is returned instead of re-executing the function.

# sunjo avi avi kuch program kiye garbeg colector avitak mitaya nehi free nahi kiya memoryko to ap dekh sakte hain keya value tha vai avi


import time

def cache(func):
    cache_value = {}
    # print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result= func(*args)
        cache_value[args] = result
        return result
    return wrapper



@cache
def long_running_function(a, b):
    time.sleep(5)
    return a + b

print(long_running_function(2, 3))
print(long_running_function(2, 3))
print(long_running_function(5, 3))










