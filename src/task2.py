import inspect, time, io
from contextlib import redirect_stdout

counts = {}

def decorator_2(func):
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
        key = func.__name__
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1

        # redirect the main processing part of the decorator
        # to be printed after printing func characterestic
        with redirect_stdout(io.StringIO()) as f:
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()


        # Printing function's characterestic
        print(f"{key} call {counts[key]} executed in  {round(end - start, 4)} sec\n")
        print("Name:    ", func.__name__)
        print("Type:    ", type(func))
        print("Sign:    ", inspect.signature(func))
        print("Doc:      ", func.__doc__ + '\n')
        print("Source:   ", inspect.getsource(func) + '\n')
        print("Output:")

        # Releasing the values of the processing
        print(f.getvalue())

        return result
        
    return wrapper