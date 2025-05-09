## Міністерство освіти і науки України

## Львівський національний університет природокористування
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №7 на тему "Використання методів класу і статичних методів"
Виконав студент групи ІТ-22
Прийняв доц. А. Татомир
### Львів 2025

## Мета роботи
Мета роботи полягає в ознайомленні з різними типами методів у об’єктно-орієнтованому програмуванні.

## Хід роботи
1. Створив [програму](oop.py), у якій є клас з *звичайними методами*, *методами класу* та *статичними методами*:
- Звичайні методи працюють з екземпляром класу (self)
- Методи класу працюють із самим класом (cls)
- Статичні методи не мають доступу ані до self, ані до cls і використовуються для допоміжних обчислень
2. Створив альтернативний конструктори з використанням декоратору `@classmethod`
3. Для класу реалізував метод класу `set_payment_amount(cls, payment_amount)`, який змінює змінну класу `payment_amount`.
4. Реалізував альтернативний конструктор `from_string(cls, bank_str)`, який дозволяє створювати об’єкт із рядка, розділеного комами.
5. Створив статичний метод `convert_usd_to_uah(usd)`, який конвертує долари США в гривні за фіксованим курсом. Перевірив його роботу незалежно від екземплярів класу.


## Висновки
В ході роботи я навчився розрізняти та застосовувати звичайні, класові та статичні методи. Реалізував метод класу для зміни змінної класу, а також альтернативний конструктор для зручного створення об’єктів із рядка. Освоїв створення та використання статичного методу для виконання додаткових обчислень, не пов’язаних безпосередньо з об’єктами чи класом.