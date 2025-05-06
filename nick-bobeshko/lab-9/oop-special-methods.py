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

    def __repr__(self):
        return f"BankModel('{self.id}','{self.first}','{self.last}','{self.email}','{self.money}')"

    def __str__(self):                          # якщо дочірній клас в self то піде в дочірній метод get_full_information()
        return self.get_full_information()
    
    @classmethod
    def from_string(cls, bank_str):
        name, last, email, initial_sum_of_money = bank_str.split(',')
        return cls(name, last, email, initial_sum_of_money)
    

    def get_full_information(self):
        return (f"[{self.id}] Full name: {self.first} {self.last}. Email: {self.email}. Sum of money: {self.money}")
    


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



prem_account1 = PremiumBankAccountModel("Derek", "Campbell", "Derek.Campbell@mail.com", 20000, "Max+")
prem_account2 = PremiumBankAccountModel("Louis", "Grant", "Louis.Grant@mail.com", 1500, "Gold")

print(prem_account2)

print(prem_account1.__repr__())
print(prem_account2.__str__())


account1 = BankModel("Cleva", "Hernandez", "Cleva.Hernandez431@clode.mef", 2000)

print(prem_account1.get_full_information())
print(account1.get_full_information())
