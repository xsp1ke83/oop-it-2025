## МІНІСТЕРСТВО ОСВІТИ І НАУКИ 
## ЛЬВІВСЬКИЙ НАЦІОНАЛЬНИЙ УНІВЕРСИТЕТ ПРИРОДОКОРИСТУВАННЯ
# Звіт
про виконання лабораторної роботи з дисципліни "Об'єктно-орієнтоване програмування" №6
на тему "Змінні класу та об’єкта."

Виконав студент групи ІТ-22 сп 
Дерпак Арсен

Прийняв доц. А.В.Татомир

Львів 2025

______________
# Мета роботи

Мета роботи – ознайомитися з різними типами змінних в об’єктно-орієнтованому програмуванні.

______________
## Хід роботи
1. Сворив [програму](lab-6-classes.py) з класом Student, який приймає аргументи *first*, *last*, *group*, *energy*, *stress_level* та ініціалізує відповідні атрибути об’єкта.
2. Реалізував метод *print_information()*, який виводить інформацію про об'єкт в консоль.
3. Реалізував метод, *linit_values()* задача якого тримати параметри класу в вірому діапазоні.
4. Реалізував методи *drink_coffe()* та *attend_clases()* які впливають на енергію та рівень стресу нашого екзепляра студента.
5. Додав класову змінну students_counter яка відповідає за збереження загальної кількості студентів.
6. Створив екземпляри класу та провів з ними кілька операцій і вивів результати в консоль.

```python
class Student:
    students_counter = 0

    def __init__(self, first, last, group, energy, stress_level):
        self.first = first
        self.last = last
        self.group = group
        self.energy = energy
        self.stress_level = stress_level
        Student.students_counter += 1

    def limit_values(self, limit):
        if self.energy < 0:
            self.energy = 0
        if self.energy > limit:
            self.energy = limit
        if self.stress_level < 0:
            self.stress_level = 0
        if self.stress_level > limit:
            self.stress_level = limit

    def drink_coffe(self):
        self.stress_level -= 1
        self.energy += 1
        self.limit_values(10)

    def attend_clases(self):
        self.stress_level += 1
        self.energy -= 2
        self.limit_values(10)
    
    def print_info(self):
        print("Full name: " + self.first + " " + self.last)
        print("Group: " + self.group)
        print("Energy: " + str(self.energy))
        print("Stress level: " + str(self.stress_level))
        print("___________________________________________")


Arsen = Student("Derpak", "Arsen", "IT_22sp", 3, 9)
Nick = Student("Bobeshko", "Mukola", "IT_22sp", 7, 5)

Arsen.print_info()
Arsen.attend_clases()
Arsen.print_info()
Arsen.drink_coffe()
Arsen.print_info()


Nick.print_info()
Nick.drink_coffe()
Nick.drink_coffe()
Nick.print_info()

print(Student.students_counter)
```
__________________

# Висновки

Під час виконання роботи я закріпив знання про роботу з класами. Дізнався про класові змінні. Попрактикувався в роботі з класами та об'єктами під час виконання практичного завдання. 