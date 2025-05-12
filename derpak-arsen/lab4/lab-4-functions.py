# In this exercise you'll use an existing function, and while adding your own to create a fully functional program.

# Add a function named list_benefits() that returns the following list of strings:
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"

# Add a function named build_sentence(info) which receives a single argument containing a string 
# and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

# Run and see all the functions work together!

import math


def f(x, y):
    res = y(x)
    print(str(x) + " : " + str(res))
    
def square_x(x):
    return x * x

def sin_x(x):
    return math.sin(x)

def sqrt_x(x):
    return math.sqrt(x)

def log_x(x):
    return math.log(x)

def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect together"]

def build_sentence(info):
    return info + " is a benefit of functions"

f(5, square_x)
f(5, sin_x)
f(5, sqrt_x)
f(5, log_x)

print(build_sentence(list_benefits()[0]))