class Car:
    car_count = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.full_name = brand + " " + model
        Car.car_count += 1  

    def describe(self):
        return "Марка: " + self.full_name + ", Рік: " + str(self.year)

    @classmethod
    def get_car_count(cls):
        return f"Кількість машин: {cls.car_count}"

car1 = Car("BMW", "X5", 2014)
car2 = Car("Tesla", "Model 3", 2023)


print(car1.describe())
print(car2.describe())
print(Car.get_car_count())
