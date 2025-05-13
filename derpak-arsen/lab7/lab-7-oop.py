class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Привіт, мене звати {self.name}, мені {self.age} років.")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_birth_year(cls, name, birth_year):
        from datetime import date
        current_year = date.today().year
        age = current_year - birth_year
        return cls(name, age)

    @classmethod
    def from_string(cls, data_str):
        name, age = data_str.split(",")
        return cls(name.strip(), int(age.strip()))


student1 = Human("Арсен", 20)
student1.greet()

print(Human.is_adult(17))

student2 = Human.from_birth_year("Микола", 2005)
student2.greet()

student3 = Human.from_string("Сергій, 19")
student3.greet()