# Клас відповідає тільки за дані користувача
class User:
    def __init__(self, name):
        self.name = name

# Клас відповідає лише за збереження інформації
class UserSaver:
    @staticmethod
    def save(user, filename="user.txt"):
        with open(filename, "w") as f:
            f.write(user.name)

# Використання
user = User("Сергій")
UserSaver.save(user)
