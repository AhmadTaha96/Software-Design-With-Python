import inspect, time, io
from contextlib import redirect_stdout

counts = {}

def decorator_4(func):
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
        try:
            key = func.__name__
            counts[key] += 1
        except KeyError: # if there is any error in the keys of the dictionary
            counts[key] = 1

        with redirect_stdout(io.StringIO()) as f:
            try:
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
            except:
                # some error may appear
                # for example if the time module was not imported well
                # print("maybe the time module was not imported well")
                import time
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()

        print(f"{key} call {counts[key]} executed in  {round(end - start, 4)} sec\n")
        print("Name:    ", func.__name__)
        print("Type:    ", type(func))
        print("Sign:    ", inspect.signature(func))
        
        try: # try block to catch any error in case the function does not have doc
            doc = func.__doc__
            print("Doc:      ", func.__doc__ + '\n')
        except:
            print("the function has no doc")
            # let the user enter the doc at the running time
            # just for showing
            # will not be added to the source code
            # doc = input("Please Enter doc string to the function")
            # func.__doc__ = doc


        print("Source:   ", inspect.getsource(func) + '\n')
        print("Output:")

        print(f.getvalue())

        return result
        
    return wrapper