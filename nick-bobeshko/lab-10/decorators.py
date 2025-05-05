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

    


class BusinessBankAccountModel(BankModel):

    def __init__(self, first, last, email, initial_sum_of_money, business_name):
        super().__init__(first, last, email, initial_sum_of_money)
        self.business_name = business_name        

    def get_full_information(self):        
        info = super().get_full_information()        
        return f"\nBusiness account info:\n\t {info}"


class PremiumBankAccountModel(BankModel):
    
    def __init__(self, first, last, email, initial_sum_of_money, premium_type):
        super().__init__(first, last, email, initial_sum_of_money)
        self.premium_type = premium_type


    def get_full_information(self):
        info = super().get_full_information()        
        return f"\nPremium account info:\n\t {info}\tPremium type: {self.premium_type}"


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
