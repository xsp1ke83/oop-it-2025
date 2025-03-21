class BankAccount:
    #Конструктор класу
    def __init__(self, owner, balance=0):
        # Властивості об'єкта
        self.owner = owner
        self.balance = balance

    # Метод для поповнення рахунку
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Рахунок поповнено на {amount}. Новий баланс: {self.balance}"
        else:
            return "Сума поповнення повинна бути більше 0."

    # Метод для зняття коштів
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Знято {amount}. Новий баланс: {self.balance}"
            else:
                return "Недостатньо коштів на рахунку."
        else:
            return "Сума зняття повинна бути більше 0."

    # Метод для отримання інформації про рахунок
    def get_balance(self):
        return f"Власник рахунку: {self.owner}, Баланс: {self.balance}"

# Створення об'єктів (екземплярів класу)
account1 = BankAccount("Микола Бобешко", 1000)
account2 = BankAccount("Тертишний Сергій", 500)

# Використання методів об'єктів
print(account1.get_balance())
print(account1.deposit(200))
print(account1.withdraw(300))
print(account1.get_balance())

print(account2.get_balance())
print(account2.deposit(100))
print(account2.withdraw(700))
print(account2.get_balance())