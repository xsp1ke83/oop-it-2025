class Car:
    
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.full_name = brand + " " + model 


    def describe(self):
        return "Марка: " + self.full_name + ", Рік: " + str(self.year)

    
car1 = Car("BMW", "X5", 2014)
car2 = Car("Tesla", "Model 3", 2023)

print(car1.describe())
print(car2.describe())


   