#програма яка:
# Запитує у користувача кількість елементів для списку.
# Заповнює список випадковими цілими числами в діапазоні від 1 до 100.
# Виводить список.
# Знаходить суму всіх парних чисел у списку.
# Знаходить добуток всіх непарних чисел у списку.
# Виводить результати.

import random

n = int(input("Введіть кількість елементів у списку: "))

random_list = [random.randint(1, 100) for _ in range(n)]
print("Згенерований список:", random_list)

sum_even = sum(x for x in random_list if x % 2 == 0)

product_odd = 1
for x in random_list:
    if x % 2 != 0:
        product_odd *= x

print("Сума парних чисел:", sum_even)
print("Добуток непарних чисел:", product_odd)