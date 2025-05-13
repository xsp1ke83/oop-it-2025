class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років.")

    def is_adult(self):
        return self.age >= 18


class Student(Human):
    def __init__(self, name, age, university, major):
        super().__init__(name, age)
        self.university = university
        self.major = major

    def introduce(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років, я студент(ка) {self.university}, спеціальність: {self.major}.")

    def study(self):
        print(f"{self.name} вивчає {self.major}.")


class Teacher(Human):
    def __init__(self, name, age, university, subject):
        super().__init__(name, age)
        self.university = university
        self.subject = subject

    def introduce(self):
        print(f"Вітаю! Я {self.name}, мені {self.age} років, я викладаю {self.subject} у {self.university}.")

    def teach(self):
        print(f"{self.name} проводить заняття з {self.subject}.")


print("=== Людина ===")
person = Human("Олександр", 30)
person.introduce()
print("Дорослий?", person.is_adult())

print("\n=== Студент ===")
student = Student("Арсен", 19, "ЛНУП", "ІТ")
student.introduce()
student.study()

print("\n=== Викладач ===")
teacher = Teacher("Ірина", 45, "КНУ", "Література")
teacher.introduce()
teacher.teach()