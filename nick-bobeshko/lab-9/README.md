## Міністерство освіти і науки України

## Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №9 на тему "Поліморфізм в Python 3"
Виконав студент групи ІТ-22 Бобешко Микола

Прийняв доц. А. Татомир
### Львів 2025

## Мета роботи
Мета роботи - засвоїти застосування принципу поліморфізму в об’єктно-орієнтованому програмуванні.

## Хід роботи
1. Створив [програму](oop-special-methods.py) в якій перевизначив поведінку `get_full_information()` для дочірніх класів `BusinessBankAccountModel` і `PremiumBankAccountModel`, розширивши вивід додатковою інформацією.
2. Реалізував декілька магічних методів у класі `BankModel`:
- `__str__(self)` — для повернення зручного текстового опису об’єкта через метод `get_full_information()`,
- `__repr__(self)` — для створення офіційного текстового представлення об’єкта, яке можна використовувати для відтворення екземпляра класу.

3. У дочірньому класі PremiumBankAccountModel реалізував власний варіант `get_full_information(self)`, який додає вивід типу преміум-акаунту (premium_type), використовуючи 
4. Перевірив роботу поліморфізму: виклик однакових методів (`get_full_information`) для об'єктів різних класів повертає різні результати залежно від конкретного класу.

Клас BankModel:
```python
class BankModel:
    number_of_accounts = 0
    payment_amount = 0 
    
    def __init__(self, first, last, email, initial_sum_of_money):
        self.first = first
        self.last = last
        self.email = email
        self.money = initial_sum_of_money
        BankModel.number_of_accounts += 1
        self.id = BankModel.number_of_accounts

    def __repr__(self):
        return f"BankModel('{self.id}','{self.first}','{self.last}','{self.email}','{self.money}')"

    def __str__(self):                      
    get_full_information()
        return self.get_full_information()
    
    @classmethod
    def from_string(cls, bank_str):
        name, last, email, initial_sum_of_money = bank_str.split(',')
        return cls(name, last, email, initial_sum_of_money)
    
    def get_full_information(self):
        return (f"[{self.id}] Full name: {self.first} {self.last}. Email: {self.email}. Sum of money: {self.money}")
    
```
Клас BusinessBankAccountModel:
```python
class BusinessBankAccountModel(BankModel):
    payment_amount = 2000

    def __init__(self, first, last, email, initial_sum_of_money, business_name):
        super().__init__(first, last, email, initial_sum_of_money)
        self.business_name = business_name        

    @classmethod
    def from_string(cls, data_str): 
        first, last, email, initial_sum_of_money, business_name = data_str.split(',')
        return cls(first, last, email, initial_sum_of_money, business_name)
        
    def get_full_information(self):
        info = super().get_full_information()        
        return f"\nBusiness account info:\n\t {info}"
```
Клас PremiumBankAccountModel:
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

    def get_full_information(self):
        info = super().get_full_information()
        
        return f"\nPremium account info:\n\t {info}\tPremium type: {self.premium_type}"        
```

## Висновки

Ознайомився з поняттям поліморфізму в об'єктно-орієнтованому програмуванні: поліморфізм дозволяє об’єктам різних класів мати методи з однаковими іменами, але з різною реалізацією.
Перевірив роботу наслідування: як дочірні класи використовують функціонал базового класу і розширюють його своїм. Освоїв використання методу super().