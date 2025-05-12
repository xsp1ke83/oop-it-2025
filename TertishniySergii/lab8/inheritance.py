class Tree:
    def __init__(self, species, age, height):
        self.species = species
        self.age = age
        self.height = height

    def grow(self, years):
        self.age += years
        self.height += years * 0.5

    def describe(self):
        return f"{self.species}, вік {self.age} років, висота {self.height:.1f} м"

# Дочірній клас FruitTree (наслідує Tree)
class FruitTree(Tree):
    def __init__(self, species, age, height, fruit_type, yield_per_year):
        super().__init__(species, age, height)  # Виклик конструктора батьківського класу
        self.fruit_type = fruit_type
        self.yield_per_year = yield_per_year

    # Перевизначений метод describe()
    def describe(self):
        base_description = super().describe()
        return f"{base_description}, плоди: {self.fruit_type} (урожайність: {self.yield_per_year} кг/рік)"

    # Новий метод, специфічний для фруктових дерев
    def harvest(self):
        return f"Зібрано {self.yield_per_year} кг {self.fruit_type}"

# Дочірній клас ForestTree (наслідує Tree)
class ForestTree(Tree):
    def __init__(self, species, age, height, wood_type):
        super().__init__(species, age, height)
        self.wood_type = wood_type

    # Перевизначений метод grow() з іншою швидкістю росту
    def grow(self, years):
        self.age += years
        self.height += years * 0.3  # Лісові дерева ростуть повільніше

# Створення об'єктів і демонстрація наслідування
apple_tree = FruitTree("Яблуня", 5, 2.5, "яблука", 50)
oak = ForestTree("Дуб", 10, 5.0, "тверда")

print(apple_tree.describe())  # Використовує перевизначений метод
print(oak.describe())        # Використовує метод батьківського класу

apple_tree.grow(2)
oak.grow(2)

print("\nПісля росту:")
print(apple_tree.describe())
print(oak.describe())  # Дуб ріс повільніше через перевизначений метод grow()

print(apple_tree.harvest())  # Виклик методу, який є тільки у FruitTree