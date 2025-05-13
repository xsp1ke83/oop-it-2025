class Tree:
    total_trees = 0  # Змінна класу

    def __init__(self, species, age, height):
        self.species = species
        self.age = age
        self.height = height
        Tree.total_trees += 1  # Збільшуємо загальну кількість дерев при створенні нового

    def grow(self, years):
        self.age += years
        self.height += years * 0.5

    def describe(self):
        return f"{self.species}, {self.age} років, {self.height:.1f} м висоти"

    @classmethod
    def get_total_trees(cls):
        return f"Всього дерев створено: {cls.total_trees}"

# Створення об'єкта
oak = Tree("Дуб", 10, 5.0)
birch = Tree("Береза", 7, 4.0)

# Збільшення віку та висоти
oak.grow(3)
birch.grow(2)

print(oak.describe())
print(birch.describe())
print(Tree.get_total_trees())  # Всього дерев створено: 2
