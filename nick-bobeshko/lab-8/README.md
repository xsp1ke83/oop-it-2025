## Міністерство освіти і науки України

## Львівський національний університет природокористування
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №8 на тему "Наслідування в об’єктно-орієнтованому програмуванні"
Виконав студент групи ІТ-22 Бобешко Микола

Прийняв доц. А. Татомир
### Львів 2025

## Мета роботи
Мета роботи - оволодіти концепцією наслідування класів.

## Хід роботи
1. Створив [програму](oop-inheritance.py) в якій є один базовий (батьківський) клас `BankModel`, який містить загальні властивості та методи для банківських акаунтів.
2. Реалізував дочірній клас `BusinessBankAccountModel`, що наслідує від `BankModel`. За допомогою методу `super()` викликав конструктор батьківського класу та додав нову властивість `business_name`. Також перевизначив змінну класу `payment_amount`, встановивши її значення на 2000.
3. Реалізував ще один дочірній клас `PremiumBankAccountModel`, який також наслідує від `BankModel`. У конструкторі через `super()` викликав ініціалізацію батьківського класу. Додав нові атрибути `premium_type` та `premium_points`.
4. У класі `PremiumBankAccountModel` створив три методи:
- `show_premium_points(self)` — для перегляду бонусних балів,
- `add_premium_points(self, amount)` — для додавання балів,
- `remove_points(self, amount)` — для їх зменшення.

```python
class PremiumBankAccountModel(BankModel):
    payment_amount = 1500

    def __init__(self, first, last, email, initial_sum_of_money, premium_type):
        super().__init__(first, last, email, initial_sum_of_money)
        self.premium_type = premium_type
        self.premium_points  = 10

    @classmethod
    def from_string(cls, data_str):
        first, last, email, initial_sum_of_money, premium_type = data_str.split(',')
        return cls(first, last, email, initial_sum_of_money, premium_type)


    def show_premium_points(self):        
        print(f"{self.first} {self.last} має {self.premium_points} бонусних балів.")        

    def add_premium_points(self, amount):
        if (amount <= 0):
            print("Помилка! Кількість бонусів не може бути менше нуля!")
            return
        self.premium_points += amount        

    def remove_points(self, amount):
        self.premium_points -= amount
```

## Висновки
Оволодів концепцією наслідування класів у Python. Перевірив роботу наслідування: як дочірні класи використовують функціонал базового класу і розширюють його своїм. Освоїв використання методу super(). Реалізував додаткові атрибути та методи в дочірніх класах. Ознайомився з методами `instanceof()`, `issubclassof()`.