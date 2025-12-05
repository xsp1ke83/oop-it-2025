class Report:
    def __init__(self, text):
        self.text = text

    def calculate_statistics(self):
        return len(self.text.split())


class ReportPrinter:
    def print(self, report: Report):
        print("Звіт:", report.text)


class ReportSaver:
    def save(self, report: Report, filename):
        with open(filename, "w") as f:
            f.write(report.text)
