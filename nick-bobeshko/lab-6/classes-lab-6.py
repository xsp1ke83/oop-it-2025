class Character:
    counter_characters = 0
    
    def __init__(self, name, damage, armor, health = 100):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor        
        Character.counter_characters += 1

    def __del__(self):
        Character.counter_characters -= 1
        print('Destructor called, Character deleted.')


    def print_information(self):
        print(f"Name: {self.name}. Health: {self.health} Armor: {self.armor}.  Damage: {self.damage}. ")
    
    
    def heal(self, amount_of_health):  # can't by more healt than 100.
        
        if (amount_of_health < 0 ):
            raise Exception("Error healt value")

        self.health += amount_of_health

        if (self.health >= 100):
            self.health = 100

    def get_hit(self, damage):

        if (damage < 0):
            raise Exception("Error healt value")

        self.health = (self.armor + self.health) - damage

        if(self.health <= 0):
            self.health = 0
            print("The character was killed.")

    

char_1 = Character("char1", 120, 40)

char_2 = Character("char2", 111, 40)

char_1.print_information()

char_1.get_hit(44)
print(char_1.health)
char_1.heal(20)

print(f" Кількість створених екземплярів: {Character.counter_characters}")

char_1.print_information()
char_2.print_information()

print(Character.counter_characters)
del char_1

print(Character.counter_characters)

