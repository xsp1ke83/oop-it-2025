class Character:
    counter_characters = 0
    
    def __init__(self, name, damage, armor, health = 100):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        
        Character.counter_characters += 1

    # @staticmethod
    def method1():
        print(f"Counter: {Character.counter_characters} ")        
        

    # def attack(self):
    #     print("Do attack..")


    # def Hit()
    def heal(self, amount_of_health):  # can't by more healt than 100.
        
        if (amount_of_health < 0 ):
            raise Exception("Error healt value")

        self.health += amount_of_health

        if (self.health >= 100):
            self.health = 100

    def get_hit(self, damage):

        if (damage < 0):
            raise Exception("Error healt value")

        self.heal = (self.armor + self.heal) - damage

        if(self.heal <= 0):
            self.heal = 0
            print("The character was killed.")

    

char_1 = Character("char1", 120, 40)
Character.method1()
char_2 = Character("char2", 111, 40)

# char_1.Attack()


print(char_1.name)

print(Character.counter_characters)