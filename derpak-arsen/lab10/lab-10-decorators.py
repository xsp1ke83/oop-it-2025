class Human:
    def __init__(self, name, surname, age):
        self._name = name
        self._surname = surname
        self.age = age

    def introduce(self):
        print(f"Привіт! Я {self.full_name}, мені {self.age} років.")

    def is_adult(self):
        return self.age >= 18

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Вік не може бути меншим за 0.")
        self._age = value

    @property
    def full_name(self):
        return f"{self._name} {self._surname}"

    @full_name.setter
    def full_name(self, value):
        parts = value.strip().split()
        if len(parts) != 2:
            raise ValueError("Повне ім’я має складатися з імені та прізвища.")
        self._name, self._surname = parts

    def __str__(self):
        return f"{self.full_name} ({self.age} років)"

    def __repr__(self):
        return f"Human(name='{self._name}', surname='{self._surname}', age={self.age})"

    def __eq__(self, other):
        return isinstance(other, Human) and self.full_name == other.full_name and self.age == other.age


class Student(Human):
    def __init__(self, name, surname, age, university, major):
        super().__init__(name, surname, age)
        self.university = university
        self.major = major

    def introduce(self):
        print(f"Привіт! Я {self.full_name}, мені {self.age} років, я студент(ка) {self.university}, спеціальність: {self.major}.")

    def study(self):
        print(f"{self._name} вивчає {self.major}.")

    def __str__(self):
        return f"Студент(ка): {self.full_name}, {self.age} років, {self.university}, спеціальність: {self.major}"


class Teacher(Human):
    def __init__(self, name, surname, age, university, subject):
        super().__init__(name, surname, age)
        self.university = university
        self.subject = subject

    def introduce(self):
        print(f"Вітаю! Я {self.full_name}, мені {self.age} років, я викладаю {self.subject} у {self.university}.")

    def teach(self):
        print(f"{self._name} проводить заняття з {self.subject}.")

    def __str__(self):
        return f"Викладач: {self.full_name}, {self.age} років, {self.university}, предмет: {self.subject}"


print("=== Тестування властивостей ===")
student = Student("Арсен", "Дерпак", 20, "ЛНУП", "ІТ")
teacher = Teacher("Ірина", "Петренко", 45, "Політехніка", "Література")

student.introduce()
teacher.introduce()

student.age = 20
teacher.full_name = "Олена Коваль"

print()
print(student)
print(teacher)

try:
    student.age = -5
except ValueError as e:
    print("Помилка при встановленні віку:", e)

try:
    teacher.full_name = "Олена"
except ValueError as e:
    print("Помилка при встановленні повного імені:", e)
