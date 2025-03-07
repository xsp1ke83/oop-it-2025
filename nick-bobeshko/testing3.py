
def f(x, y):
    res = y(x)
    print(str(x) + " : " + str(res))
    
def y(x):
    return x * x


f(7, y)