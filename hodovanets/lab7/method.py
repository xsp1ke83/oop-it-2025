class Car:
    car_count = 0

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.full_name = brand + " " + model
        Car.car_count += 1

    def describe(self):
        return f"Марка: {self.full_name}, Рік: {self.year}"

    @classmethod
    def get_car_count(cls):
        return f"Всього машин: {cls.car_count}"

    @classmethod
    def from_string(cls, car_str):
        brand, model, year = car_str.split("-")
        return cls(brand, model, int(year))

    @staticmethod
    def is_old(year):
        return year < 2015

car1 = Car("Ford", "Focus", 2010)
car2 = Car.from_string("Tesla-ModelX-2022")


print(car1.describe())
print(car2.describe())
print(Car.get_car_count())
print("car1", Car.is_old(car1.year))
print("car2", Car.is_old(car2.year))