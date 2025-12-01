class User:
    def __init__(self, name):
        self.name = name

    def save_to_file(self):
        with open("user.txt", "w") as f:
            f.write(self.name)
#--Проблема:
#Клас і зберігає дані, і описує модель користувача.