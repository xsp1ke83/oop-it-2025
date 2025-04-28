class BankModel:
    number_of_accounts = 0
    payment_amount = 0      # сума для виплат
    
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
        

    def __repr__(self):
        return f"BankModel('{self.id}','{self.first}','{self.last}','{self.__email}','{self.money}')"

    def __str__(self):                        
        return self.get_full_information()

    @classmethod
    def from_string(cls, bank_str):
        name, last, email, initial_sum_of_money = bank_str.split(',')
        return cls(name, last, email, initial_sum_of_money)
    

    def get_full_information(self):
        return (f"[{self.id}] Full name: {self.first} {self.last}. Email: {self.__email}. Sum of money: {self.money}")
    
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

    def __init__(self, first, last, email, initial_sum_of_money, business_name):
        super().__init__(first, last, email, initial_sum_of_money)
        self.business_name = business_name        

    @classmethod
    def from_string(cls, data_str):     # first, last, email, initial_sum_of_money, business_name
        first, last, email, initial_sum_of_money, business_name = data_str.split(',')
        return cls(first, last, email, initial_sum_of_money, business_name)
        
    def get_full_information(self):
        
        info = super().get_full_information()        
        return f"\nBusiness account info:\n\t {info}"

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
        # return "\nPremium account info:\n" + info + f"\n Premium type: {}"

    def show_premium_points(self):        
        print(f"{self.first} {self.last} має {self.premium_points} бонусних балів.")        

    def add_premium_points(self, amount):
        if (amount <= 0):
            print("Помилка! Кількість бонусів не може бути менше нуля!")
            return
        self.premium_points += amount        

    def remove_points(self, amount):
        self.premium_points -= amount


prem_account1 = PremiumBankAccountModel("Derek", "Campbell", "Derek.Campbell@mail.com", 20000, "Max+")
prem_account2 = PremiumBankAccountModel("Louis", "Grant", "Louis.Grant@mail.com", 1500, "Gold")

print(prem_account2)
 
# account1 = BankModel("Cleva", "Hernandez", "Cleva.Hernandez431@clode.mef", 2000)

print(prem_account1.get_full_information())
prem_account1.email = "fewfwe@mail.tm"
prem_account1.email = "grang32d@exp.io"
prem_account1.email = "kaliavn_h12@meta.ua"

print(prem_account1.email)
print(prem_account1.email_history)
# print(account1.get_full_information())
