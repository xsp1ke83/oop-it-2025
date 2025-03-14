# Програма, яка:
# Запитує у користувача два числа.
# Виконує базові арифметичні операції (додавання, віднімання, множення, ділення) з цими числами та виводить результати.
# Порівнює ці числа та виводить результати порівняння (більше, менше, дорівнює).
# Перевіряє, парні чи не парні числа.

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

sum_result = num1 + num2
diff_result = num1 - num2
prod_result = num1 * num2
div_result = num1 / num2

print(f"Сума: {num1} + {num2} = {sum_result}")
print(f"Різниця: {num1} - {num2} = {diff_result}")
print(f"Добуток: {num1} * {num2} = {prod_result}")
print(f"Частка: {num1} / {num2} = {div_result}")

if num1 > num2:
    print(f"{num1} більше за {num2}")
elif num1 < num2:
    print(f"{num1} менше за {num2}")
else:
    print(f"{num1} дорівнює {num2}")

if num1 % 2 == 0 and num2 % 2 == 0:
    print("Обидва числа парні")
elif num1 % 2 != 0 and num2 % 2 != 0:
    print("Обидва числа непарні")
else:
    print("Одне число парне, а інше непарне")