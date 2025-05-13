from abc import ABC, abstractmethod
# Базовий абстрактний клас
class Plant(ABC):
    def __init__(self, species, age):
        self.species = species
        self.age = age
    
    @abstractmethod
    def grow(self, years):
        pass
    
    @abstractmethod
    def get_info(self):
        pass

class Tree(Plant):
    def __init__(self, species, age, height):
        super().__init__(species, age)
        self.height = height
    
    def grow(self, years):
        self.age += years
        self.height += years * 0.5
        return f"{self.species} виріс на {years} роки"
    
    def get_info(self):
        return f"Дерево {self.species}, {self.age} років, висота {self.height:.1f} м"

class FruitTree(Tree):
    def __init__(self, species, age, height, fruit_type):
        super().__init__(species, age, height)
        self.fruit_type = fruit_type
    
    def grow(self, years):  # Перевизначення методу
        super().grow(years)
        return f"{self.species} виріс на {years} роки і дасть більше {self.fruit_type}"
    
    def harvest(self):  # Унікальний метод
        return f"Зібрано {self.fruit_type}"

# Новий клас для демонстрації поліморфізму
class Bush(Plant):
    def __init__(self, species, age, diameter):
        super().__init__(species, age)
        self.diameter = diameter
    
    def grow(self, years):  # Інша реалізація
        self.age += years
        self.diameter += years * 0.2
        return f"{self.species} розрісся вшир"
    
    def get_info(self):
        return f"Кущ {self.species}, {self.age} років, діаметр {self.diameter:.1f}м"

# Поліморфна функція для роботи з рослинами
def plant_care(plants, years):
    for plant in plants:
        print(plant.grow(years))
        print(plant.get_info())
        if isinstance(plant, FruitTree):
            print(plant.harvest())
        print("-" * 30)

# Створення об'єктів різних класів
plants = [
    Tree("Дуб", 10, 5.0),
    FruitTree("Яблуня", 5, 2.5, "яблук"),
    Bush("Аґрус", 3, 1.2)
]

# Демонстрація поліморфізму
plant_care(plants, 2)

# Поліморфізм операторів через __add__
class Forest:
    def __init__(self, plants):
        self.plants = plants
    
    def __add__(self, other):
        return Forest(self.plants + other.plants)
    
    def show_plants(self):
        for plant in self.plants:
            print(f"- {plant.get_info()}")

# Використання
forest1 = Forest([plants[0], plants[1]])
forest2 = Forest([plants[2]])
combined_forest = forest1 + forest2  # Поліморфізм оператора +
print("\nКомбінований ліс:")
combined_forest.show_plants()