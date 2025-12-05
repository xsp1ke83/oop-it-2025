# ---------------- Observer Pattern -----------------

class Observer:
    def update(self, message: str):
        raise NotImplementedError()


class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for obs in self._observers:
            obs.update(message)


# ----- Конкретний суб'єкт -----
class NewsAgency(Subject):
    def new_news(self, text: str):
        print(f"\nНовина опублікована: {text}")
        self.notify(text)


# ----- Конкретні спостерігачі -----
class EmailSubscriber(Observer):
    def update(self, message: str):
        print(f"Email: отримано новину — {message}")


class SMSSubscriber(Observer):
    def update(self, message: str):
        print(f"SMS: отримано новину — {message}")


# ----- Використання -----
if __name__ == "__main__":
    agency = NewsAgency()

    email = EmailSubscriber()
    sms = SMSSubscriber()

    agency.attach(email)
    agency.attach(sms)

    agency.new_news("Шаблони проєктування — це легко!")
