class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.full_name = brand + " " + model

    def describe(self):
        return "Марка: " + self.full_name + ", Рік: " + str(self.year)

    def __str__(self):
        return f"{self.full_name} ({self.year})"

    def __eq__(self, other):
        return self.brand == other.brand and self.model == other.model and self.year == other.year

    def __len__(self):
        return len(self.full_name)

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity

    def describe(self):
        base = super().describe()
        return base + f", Батарея: {self.battery_capacity} кВт⋅год"
car1 = Car("BMW", "X5", 2014)
car2 = ElectricCar("Tesla", "Model 3", 2023, 75)
car3 = Car("BMW", "X5", 2014)

print(car1.describe())        
print(car2.describe())         
print(str(car1))               
print(car1 == car3)            
print(len(car2))               
