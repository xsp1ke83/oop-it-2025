# Subject (об'єкт, за яким спостерігають)
class Light:
    def __init__(self):
        self.observers = []
        self.state = "OFF"

    def add_observer(self, observer):
        self.observers.append(observer)

    def set_state(self, new_state):
        self.state = new_state
        self.notify()

    def notify(self):
        for obs in self.observers:
            obs.update(self.state)

# Observer (спостерігач)
class Display:
    def update(self, state):
        print(f"Дисплей: стан ліхтарика - {state}")

# Використання
light = Light()
screen = Display()

light.add_observer(screen)

light.set_state("ON")
light.set_state("OFF")
