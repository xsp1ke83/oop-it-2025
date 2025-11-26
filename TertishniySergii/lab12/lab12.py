# Старий принтер з несумісним інтерфейсом
class OldPrinter:
    def old_print(self, text):
        return f"Old printer prints: {text}"

# Новий інтерфейс, який очікує клієнт
class PrinterInterface:
    def print(self, text):
        raise NotImplementedError

# Адаптер: робить OldPrinter сумісним з новим інтерфейсом
class PrinterAdapter(PrinterInterface):
    def __init__(self, old_printer):
        self.old_printer = old_printer

    def print(self, text):
        return self.old_printer.old_print(text)

old_printer = OldPrinter()
adapter = PrinterAdapter(old_printer)

print(adapter.print("Hello world!"))
