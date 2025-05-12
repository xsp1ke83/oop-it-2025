class Tree:
    total_trees = 0

    def __init__(self, species, age, height):
        self.species = species      # вид дерева
        self.age = age              # вік у роках
        self.height = height        # висота в метрах
        Tree.total_trees += 1       # збільшуємо лічильник при створенні нового об'єкта

    def grow(self, years):
        self.age += years
        self.height += years * 0.5  # дерево росте на 0.5 м щороку

    def describe(self):
        return f"{self.species}, {self.age} років, {self.height:.1f} м висоти"

    # Метод класу для роботи зі змінною класу
    @classmethod
    def get_total_trees(cls):
        return f"Всього дерев створено: {cls.total_trees}"

    # Альтернативний конструктор
    @classmethod
    def from_height_in_feet(cls, species, age, height_feet):
        # Конвертуємо фути в метри (1 фут = 0.3048 метра)
        height_meters = height_feet * 0.3048
        return cls(species, age, height_meters)

    # Статичний метод
    @staticmethod
    def is_old_tree(age):
        """Статичний метод, який визначає, чи вважається дерево старим (вік > 50 років)"""
        return age > 50

oak = Tree("Дуб", 10, 5.0)
birch = Tree("Береза", 7, 4.0)

oak.grow(3)
birch.grow(2)

print(oak.describe())
print(birch.describe())

# Використання методу класу для отримання загальної кількості дерев
print(Tree.get_total_trees())  # Всього дерев створено: 2

# Використання альтернативного конструктора
pine = Tree.from_height_in_feet("Сосна", 15, 20)  # висота 20 футів
print(pine.describe())  # Сосна, 15 років, 6.1 м висоти

# Використання статичного методу >50
print(Tree.is_old_tree(60))  
print(Tree.is_old_tree(30))  
print(pine.is_old_tree(pine.age))