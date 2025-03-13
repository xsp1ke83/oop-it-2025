class Vehicle:
    def __init__(self, name: str, color: str, kind: str, value: float = 100.00):
        self.name = name
        self.color = color
        self.kind = kind
        self.value = value

    def description(self, detailed: bool = False) -> str:
        if detailed:
            return f"🚗 {self.name} is a stylish {self.color} {self.kind}, priced at ${self.value:,.2f}!"
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:,.2f}."
    
car1 = Vehicle(name="Fer", color="red", kind="convertible", value=60000.00)
car2 = Vehicle(name="Jump", color="blue", kind="van", value=10000.00)


print(car1.description(detailed=True))
print(car2.description(detailed=True))
