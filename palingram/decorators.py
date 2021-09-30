"""decorator module for evaluating function running time"""
from functools import wraps
from time import time

def elaspsed_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):        
        start_time = time()
        res = func(*args, **kwargs)
        end_time = time()
        print(f"elasped time : {end_time - start_time}")
        return res
    return wrapper
