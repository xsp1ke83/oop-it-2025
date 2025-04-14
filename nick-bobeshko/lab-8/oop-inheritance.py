class BankModel:
    number_of_accounts = 0
    payment_amount = 0      # сума для виплат
    
    def __init__(self, first, last, email, initial_sum_of_money):
        self.first = first
        self.last = last
        self.email = email
        self.money = initial_sum_of_money
        BankModel.number_of_accounts += 1
        self.id = BankModel.number_of_accounts

    @classmethod
    def from_string(cls, bank_str):
        name, last, email, initial_sum_of_money = bank_str.split(',')
        return cls(name, last, email, initial_sum_of_money)
    

    def print_full_information(self):
        print(f"[{self.id}] Full name: {self.first} {self.last}. Email: {self.email}. Sum of money: {self.money}\n")
    
    @classmethod
    def set_payment_amount(cls, payment_amount):
        cls.payment_amount = payment_amount

    def apply_payment(self):
        self.money += self.payment_amount

    @staticmethod
    def convert_usd_to_uah(usd): # usd to uah
        return usd * 41.48


class BusinessBankAccountModel(BankModel):
    payment_amount = 2000
    # business_points = 0

    def __init__(self, first, last, email, initial_sum_of_money, business_name):
        super().__init__(first, last, email, initial_sum_of_money)
        self.business_name = business_name        

    @classmethod
    def from_string(cls, data_str):     # first, last, email, initial_sum_of_money, business_name
        first, last, email, initial_sum_of_money, business_name = data_str.split(',')
        return cls(first, last, email, initial_sum_of_money, business_name)

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


account1 = PremiumBankAccountModel("Derek", "Campbell", "Derek.Campbell@mail.com", 20000, "Max+")
account2 = PremiumBankAccountModel("Louis", "Grant", "Louis.Grant@mail.com", 1500, "Gold")

account1.apply_payment()

account1.print_full_information()
account2.print_full_information()
print(account1.premium_type)
print(account2.premium_type)


account1.show_premium_points()
account1.add_premium_points(20)
account1.remove_points(2)
account1.show_premium_points()

account1.print_full_information()

account = BankModel("Joe", "Morrison", "joe.morrisonf343@mail.com", 1400)

account.print_full_information()


bsns_account1 = BusinessBankAccountModel.from_string("Victorine,Tucker,victorine.fer@gmail.com,1500,Victine.Corp")
prem_account1 = PremiumBankAccountModel.from_string("Victorine,Tucker,victorine.fer@gmail.com,1500,Max++")


prem_account1.print_full_information()

print(isinstance(prem_account1, BusinessBankAccountModel))

print(issubclass(PremiumBankAccountModel, BankModel) )


