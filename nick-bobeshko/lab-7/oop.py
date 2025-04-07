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

    def print_full_information(self):
        print(f"[{self.id}] Full name: {self.first} {self.last}. Email: {self.email}. Sum of money: {self.money}\n")
    
    @classmethod
    def set_payment_amount(cls, payment_amount):
        BankModel.payment_amount = payment_amount

    def apply_payment(self):
        self.money += BankModel.payment_amount

    @staticmethod
    def convert_usd_to_uah(usd): # usd to uah
        return usd * 41.48


account1 = BankModel("Nick", "Brooks", "nickerf.greger@mail.com", 500)
account2 = BankModel("Romeo", "Hemingway", "Romeo.Hemingway@mail.com", 1000)

account1.print_full_information()

BankModel.set_payment_amount(123)

account1.apply_payment()

account1.print_full_information()
account2.print_full_information()

print( BankModel.convert_usd_to_uah(20) )

print(account1.convert_usd_to_uah(19))
