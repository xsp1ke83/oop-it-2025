class Tree:
    def __init__(self, species, age, height):
        self.species = species      # вид дерева
        self.age = age              # вік у роках
        self.height = height        # висота в метрах

    def grow(self, years):
        self.age += years
        self.height += years * 0.5  # дерево росте на 0.5 м щороку

    def describe(self):
        return f"{self.species}, {self.age} років, {self.height:.1f} м висоти"

# Створення об'єкта
oak = Tree("Дуб", 10, 5.0)
birch = Tree("Береза", 7, 4.0)

# Збільшення віку та висоти
oak.grow(3)
birch.grow(2)

print(oak.describe())
print(birch.describe())