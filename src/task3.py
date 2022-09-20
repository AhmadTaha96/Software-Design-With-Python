import inspect, time
from prettytable import PrettyTable

# dictionaries to hold the time taken for each value and trace of each function
time_taken, counts = dict(), dict()

class decorator_3(object):

    def __init__(self, arg):

        # getting the name of function to be decorated to be part of decorator class
        self.__arg = arg

    def __call__(self, *args, **kwargs):

        global counts
        start = time.time()
        result = self.__arg(*args, **kwargs)
        end = time.time()

        # First time call of this function
        if self.__arg.__name__ not in time_taken:
            time_taken[self.__arg.__name__] = round(end - start, 4)
            counts[self.__arg.__name__] = 1
        else:
            # Updating step
            time_taken[self.__arg.__name__] = round(end - start, 4)
            counts[self.__arg.__name__] += 1            
        
        # Dumping the output to the file test_file.txt (appending)
        with open("test_file.txt", 'a') as f:
            f.write("Name: " + str(self.__arg.__name__) + '\n')
            f.write("Type: " + str(type(self.__arg)) + '\n')
            f.write("Sign: " + str(inspect.signature(self.__arg)) + '\n')
            f.write("Doc: " + str(self.__arg.__doc__)+ '\n')
            f.write("Sorce: " + '\n' + str(inspect.getsource(self.__arg)) + '\n')

        return result

    # function to release the time of each function as prettytable output
    # to be called by the decorator class object
    def get_time():
        global time_taken
        # sort time taken due to value (not the keys)
        time_taken = sorted(time_taken.items(), key = lambda x : x[1])
        t = PrettyTable(["PROGRAM", "RANK", "TIME ELAPSED"])
        i = 1
        for item in time_taken:
            t.add_row([item[0], i, item[1]])
            i += 1

        print(counts)
        print(t)