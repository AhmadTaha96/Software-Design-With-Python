import inspect, time, io
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

# Applying the first task
print("Applying the first task")

@decorator_1
def pascal(n):
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_1
def solver():
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

# Test the first function
print(pascal(5))

# Test the second function
print(solver()(1, 2, 0))


print("\n\n")

# Applying the second task
print("Applying the second task")

@decorator_2
def pascal(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_2
def solver():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))


# Test the first function
print(pascal(5))
# Test the second function
print(solver()(1, 2, 0))

print("\n\n")

# Applying the third task
print("Applying the third task")

@decorator_3
def pascal(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_3
def solver():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))


# Test the first function
print(pascal(5))
# Test the second function
print(solver()(1, 2, 0))

# Call by the decorator class itself (not an instance)
decorator_3.get_time()

print("\n\n")

# Applying the fourth task
print("Applying the fourth task")
print("Basically same output as the second task")

@decorator_4
def pascal(n):
	"""
	Function to print the first n rows of pascal triangle

	Parameters:
	n: number of rows we want to print
	"""
	# n is the number of rows we want the program to print
	return [(lambda s: [s] + [s := s * (r - t) // (t + 1) for t in range(r)])(1) for r in range(n)]


@decorator_4
def solver():
	"""
	Function to solve quadratic equation

	Parameters:
	a, b, c: in the same order from the highest degree term to the lowest degree term
	"""
	# the arguemet will not pass to the solver
	return lambda a, b, c: ((-b + sqrt((b * b) - (4 * a * c))) / (2 * a), (-b - sqrt((b * b) - (4 * a * c))) / (2 * a))

pascal(4)
print(solver()(1,2,0))