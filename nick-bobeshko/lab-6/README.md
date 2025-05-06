## Міністерство освіти і науки України

## Львівський національний університет природокористування
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №6 на тему "Змінні класу та об’єкта."
Виконав студент групи ІТ-22
Прийняв доц. А. Татомир
### Львів 2025

## Мета роботи
Мета роботи – ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні.

## Хід роботи
1. Сворив [програму](classes-lab-6.py) у якій є клас Character, який приймає аргументи *name*, *damage*, *armor*, *health* та ініціалізує відповідні атрибути об’єкта.
2. Реалізував метод *print_information(self)*, який генерує опис об’єкта, виводячи його основні характеристики.
3. Створив екземпляри класу: створив декілька об’єктів *Character*, викликав для них метод *print_information()*.
4. Реалізував методи *heal(self, amount_of_health)*, який збільшує здоров’я персонажа, та *get_hit(self, damage)*, який враховує броню при отриманні шкоди.

```
class Character:
    counter_characters = 0
    
    def __init__(self, name, damage, armor, health = 100):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor        
        Character.counter_characters += 1

    def __del__(self):
        Character.counter_characters -= 1
        print('Destructor called, Character deleted.')


    def print_information(self):
        print(f"Name: {self.name}. Health: {self.health} Armor: {self.armor}.  Damage: {self.damage}. ")
    
    
    def heal(self, amount_of_health):  # can't by more healt than 100.
        
        if (amount_of_health < 0 ):
            raise Exception("Error healt value")

        self.health += amount_of_health

        if (self.health >= 100):
            self.health = 100

    def get_hit(self, damage):

        if (damage < 0):
            raise Exception("Error healt value")

        self.health = (self.armor + self.health) - damage

        if(self.health <= 0):
            self.health = 0
            print("The character was killed.")
```

## Висновки
В ході роботи я навчився створювати класи, оголошувати їхні атрибути та методи, дізнався про різницю атрибутів класу та екземпляру. Засвоїв принципи використання змінних класу та створив лічильник об’єктів. Реалізував функціональність для роботи з об’єктами класу.