from datetime import datetime

# Декоратор для логування часу виклику методу
def log_method(func):
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Викликано метод {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Декоратор для перевірки віку дерева
def validate_age(min_age=0, max_age=1000):
    def decorator(func):
        def wrapper(self, years, *args, **kwargs):
            if self.age + years < min_age:
                raise ValueError(f"Вік не може бути меншим за {min_age} років")
            if self.age + years > max_age:
                raise ValueError(f"Вік не може бути більшим за {max_age} років")
            return func(self, years, *args, **kwargs)
        return wrapper
    return decorator

class Tree:
    def __init__(self, species, age, height):
        self.species = species
        self.age = age
        self.height = height
    
    @log_method
    @validate_age(min_age=1, max_age=500)
    def grow(self, years):
        """Метод для зростання дерева"""
        self.age += years
        self.height += years * 0.5
        return f"{self.species} виріс на {years} років. Тепер його висота: {self.height:.1f} м"
    
    @log_method
    def get_info(self):
        """Метод для отримання інформації"""
        return f"{self.species}, {self.age} років, {self.height:.1f} м"

# Створення та тестування об'єкта
oak = Tree("Дуб", 50, 10.0)

print(oak.grow(10))  # Працює коректно
print(oak.get_info())

try:
    print(oak.grow(450))  #помилка (50 + 450 > 500)
except ValueError as e:
    print(f"Помилка: {e}")