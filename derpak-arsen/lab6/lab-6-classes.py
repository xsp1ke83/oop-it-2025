class Student:
    students_counter = 0

    def __init__(self, first, last, group, energy, stress_level):
        self.first = first
        self.last = last
        self.group = group
        self.energy = energy
        self.stress_level = stress_level
        Student.students_counter += 1

    def limit_values(self, limit):
        if self.energy < 0:
            self.energy = 0
        if self.energy > limit:
            self.energy = limit
        if self.stress_level < 0:
            self.stress_level = 0
        if self.stress_level > limit:
            self.stress_level = limit

    def drink_coffe(self):
        self.stress_level -= 1
        self.energy += 1
        self.limit_values(10)

    def attend_clases(self):
        self.stress_level += 1
        self.energy -= 2
        self.limit_values(10)
    
    def print_info(self):
        print("Full name: " + self.first + " " + self.last)
        print("Group: " + self.group)
        print("Energy: " + str(self.energy))
        print("Stress level: " + str(self.stress_level))
        print("___________________________________________")


Arsen = Student("Derpak", "Arsen", "IT_22sp", 3, 9)
Nick = Student("Bobeshko", "Mukola", "IT_22sp", 7, 5)

Arsen.print_info()
Arsen.attend_clases()
Arsen.print_info()
Arsen.drink_coffe()
Arsen.print_info()


Nick.print_info()
Nick.drink_coffe()
Nick.drink_coffe()
Nick.print_info()

print(Student.students_counter)

