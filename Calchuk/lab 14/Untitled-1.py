class Report:
    def __init__(self, text):
        self.text = text

    def calculate_statistics(self):
        # якісь статистичні обчислення
        return len(self.text.split())

    def print_report(self):
        print("Звіт:", self.text)

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            f.write(self.text)
