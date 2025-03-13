def list_benefits():
    return [
        "Зручніша організація коду",
        "Покращена читабельність коду",
        "Спрощене повторне використання коду",
        "Можливість обмінюватися та поєднувати код"
    ]

def build_sentence(benefit):
    return f"{benefit} — це перевага використання функцій!"


def show_benefits():
    for benefit in list_benefits():
        print(build_sentence(benefit))


show_benefits()
