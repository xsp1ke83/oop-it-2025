class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років.")

    def is_adult(self):
        return self.age >= 18

    def __str__(self):
        return f"{self.name} ({self.age} років)"

    def __repr__(self):
        return f"Human(name='{self.name}', age={self.age})"

    def __eq__(self, other):
        return isinstance(other, Human) and self.name == other.name and self.age == other.age


class Student(Human):
    def __init__(self, name, age, university, major):
        super().__init__(name, age)
        self.university = university
        self.major = major

    def introduce(self):
        print(f"Привіт! Я {self.name}, мені {self.age} років, я студент(ка) {self.university}, спеціальність: {self.major}.")

    def study(self):
        print(f"{self.name} вивчає {self.major}.")

    def __str__(self):
        return f"Студент(ка): {self.name}, {self.age} років, {self.university}, спеціальність: {self.major}"


class Teacher(Human):
    def __init__(self, name, age, university, subject):
        super().__init__(name, age)
        self.university = university
        self.subject = subject

    def introduce(self):
        print(f"Вітаю! Я {self.name}, мені {self.age} років, я викладаю {self.subject} у {self.university}.")

    def teach(self):
        print(f"{self.name} проводить заняття з {self.subject}.")

    def __str__(self):
        return f"Викладач: {self.name}, {self.age} років, {self.university}, предмет: {self.subject}"


# === Поліморфізм ===
print("=== Демонстрація поліморфізму ===")
people = [
    Human("Олександр", 30),
    Student("Марія", 19, "Політехніка", "Філологія"),
    Teacher("Ірина", 45, "ЛНУП", "Література")
]

for person in people:
    person.introduce()

print("\n=== Демонстрація магічних методів ===")

s1 = Student("Арсен", 19, "Лнуп", "ІТ")
s2 = Student("Арсен", 19, "Лнуп", "ІТ")
t1 = Teacher("Ірина", 45, "Медичний", "Біологія")

print(str(s1))
print(repr(t1))
print("s1 == s2:", s1 == s2)

# Додатково
print("\n=== Методи класів ===")
s1.study()
t1.teach()