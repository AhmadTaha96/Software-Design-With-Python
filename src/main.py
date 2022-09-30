import inspect, time, io, random
from math import sqrt
from contextlib import redirect_stdout
from prettytable import PrettyTable
from task1 import decorator_1
from task2 import decorator_2
from task3 import decorator_3
from task4 import decorator_4

# Function pascal definition without decoration
# def pascal(n):
# 	# n is the number of rows we want the program to print
# 	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]

# Function solver definition without decoration
# def solver():
# 	# the arguemet will not pass to the solver
# 	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

@decorator_1
def pascal1(n):
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_1
def solver1():
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

@decorator_1
def funcx1(a = 2, b = 5):
    """funx just for testing"""
    print("Processing...")
    
    n, r =  random.randint(10,751), random.randint(10,751)
    res = [i ** 2 for i in range(n)]
    c = 0
    for i in res:
        if i > r: 
            c += 1

@decorator_2
def pascal2(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_2
def solver2():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))


@decorator_2
def funcx2(a = 2, b = 5):
    """funx just for testing"""
    print("Processing...")
    
    n, r =  random.randint(10,751), random.randint(10,751)
    res = [i ** 2 for i in range(n)]
    c = 0
    for i in res:
        if i > r: 
            c += 1

@decorator_3
def pascal3(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_3
def solver3():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))


@decorator_3
def funcx3(a = 2, b = 5):
    """funx just for testing"""
    print("Processing...")
    
    n, r =  random.randint(10,751), random.randint(10,751)
    res = [i ** 2 for i in range(n)]
    c = 0
    for i in res:
        if i > r: 
            c += 1

@decorator_4
def pascal4(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_4
def solver4():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

@decorator_4
def funcx4(a = 2, b = 5):
    """funx just for testing"""
    print("Processing...")
    
    n, r =  random.randint(10,751), random.randint(10,751)
    res = [i ** 2 for i in range(n)]
    c = 0
    for i in res:
        if i > r: 
            c += 1

if __name__ == "__main__":

	answer = int(input("Enter the number of decorator you want to test "))

	if answer == 1:
		print("Applying the first task")
		print(pascal1(5))
		print(pascal1(5))		
		result = solver1()(1, 2, 0)
		print("the first root =", result[0])
		print("the second root =", result[1])
		result = solver1()(1, 2, 0)
		print("the first root =", result[0])
		print("the second root =", result[1])
		funcx1(1, 100)
		funcx1(1, 100)
		funcx1(1, 100)

	if answer == 2:
		print("Applying the second task")		
		print(pascal2(5))
		result = solver2()(1, 2, 0)
		print("the first root =", result[0])
		print("the second root =", result[1])
		funcx2(1, 100)

	if answer == 3:
		print("Applying the third task")
		print(pascal3(5))
		print(pascal3(5))
		result = solver3()(1, 2, 0)
		result = solver3()(1, 2, 0)
		print("the first root =", result[0])
		print("the second root =", result[1])
		funcx3(1, 100)
		funcx3(1, 100)
		funcx3(1, 100)
		# Call by the decorator class itself (not an instance)
		decorator_3.get_time()

	if answer == 4:
		print("Applying the fourth task")		
		print(pascal4(5))
		result = solver4()(1, 2, 0)
		print("the first root =", result[0])
		print("the second root =", result[1])
		funcx4(1, 100)