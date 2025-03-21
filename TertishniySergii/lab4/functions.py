#Створення функції з параметрами
def greet(name):
    return f"Привіт, {name}!"

#Функція, яка приймає іншу функцію як аргумент (callback)
def call_function(func, arg):
    return func(arg)

#Функція, яка повертає іншу функцію
def create_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

#Виклик функцій
if __name__ == "__main__":
 
    greeting = greet("Студент")
    print(greeting)  


    result = call_function(greet, "Сергію")
    print(result)  

    #Використання функції, яка повертає іншу функцію
    double = create_multiplier(2)
    triple = create_multiplier(3)

    print(double(5)) 
    print(triple(5)) 