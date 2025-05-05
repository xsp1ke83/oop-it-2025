class Car:
    
    def __init__(self, brand, model, year):
        self._brand = brand
        self._model = model
        self.year = year

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        self._model = value

    @property
    def full_name(self):
        return self.brand + " " + self.model

    def describe(self):
        return "Марка: " + self.full_name + ", Рік: " + str(self.year)

car1 = Car("BMW", "X5", 2014)
car2 = Car("Tesla", "Model 3", 2023)

print(car1.describe())    
print(car2.describe())    

car1.model = "X6"         
print(car1.describe())
