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

f(5, square_x)
f(5, sin_x)
f(5, sqrt_x)
f(5, log_x)


