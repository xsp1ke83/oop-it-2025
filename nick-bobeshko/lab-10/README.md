## Міністерство освіти і науки України

## Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №10 на тему "Використання декораторів методів"
Виконав студент групи ІТ-22 Бобешко Микола

Прийняв доц. А. Татомир
### Львів 2025

## Мета роботи
Мета роботи - освоїти роботу з декораторами в Python 3.

## Хід роботи
1. Створив [програму](decorators.py) з класом `BankModel` властивість email через декоратор `@property`, що дозволяє працювати з `email` як із звичайним атрибутом.
2. Створив getter для отримання актуальної адреси електронної пошти користувача.
3. Створив `setter`, який дозволяє змінювати адресу електронної пошти з базовою валідацією (наявність символу @) та автоматичним збереженням історії змін електронної пошти у списку `email_history`.

```
class BankModel:
    number_of_accounts = 0    
    
    def __init__(self, first, last, email, initial_sum_of_money):
        self.first = first
        self.last = last
        self.__email = email
        self.money = initial_sum_of_money
        BankModel.number_of_accounts += 1
        self.id = BankModel.number_of_accounts
        self.email_history = [email] 

    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if ("@") in email:
            self.__email = email
            self.email_history.append(email)            
        else:
            raise ValueError("Invalid email address.")
```

## Висновки
У ході роботи я навчився використовувати декоратор `@property` для створення контрольованого доступу до атрибутів об'єкта. Засвоїв концепцію геттерів і сеттерів у Python та реалізував їх для властивості email у класі `BankModel`. 

Дізнався про те що до атрибута з двома підкресленнями не можна звернутися ззовні (private атрибут) - `(self.__first_name)`.