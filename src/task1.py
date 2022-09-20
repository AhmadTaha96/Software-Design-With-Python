import time

# dictionary to hold how many times each function was called
counts = {}

def decorator_1(func):
    """
    A decorator function that calculate the execution time of some function
    and the trace of the function (number of times decorator was called)
    
    Parameters:   
    func: The function being decorated (called).
 
    Returns:  
    The decorated function (func)
    """
    def wrapper(*args, **kwargs):
        global counts
        # getting the function name (func) which we will pass to the decorator
        key = func.__name__
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1

        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print(f"{key} call {counts[key]} executed in  {round(end - start, 4)} sec")
        return result
    
    return wrapper