# Програма, яка:
# Створює словник, де ключами є назви товарів, а значеннями — їх ціни.
# Додає новий товар до словника.
# Видаляє товар за назвою.
# Змінює ціну для певного товару.
# Обчислює загальну вартість всіх товарів у словнику.

products = {
    "яблука": 10.5,
    "банани": 15.0,
    "молоко": 22.3,
    "хліб": 12.0
}
print("Початковий словник товарів:", products)

products["кава"] = 45.0
print("Словник після додавання кави:", products)

del products["банани"]
print("Словник після видалення бананів:", products)

products["молоко"] = 20.0
print("Словник після зміни ціни на молоко:", products)

print("Остаточний словник товарів:", products)

total_cost = sum(products.values())
print("Загальна вартість всіх товарів:", total_cost)