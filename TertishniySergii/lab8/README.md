## Міністерство освіти і науки України  
## Львівський національний університет ветеринарної медицини та біотехнологій імені С.З. Ґжицького
## Звіт 
### про виконання лабораторної роботи з дисципліни: <br> Об'єктно-орієнтоване програмування 
### Лабораторна робота №8 на тему <br> "Наслідування в об’єктно-орієнтованому програмуванні"
Виконав студент групи ІТ-22СП <br> Тертишний Сергій
<br> Прийняв доц. А. Татомир

#### Львів 2025

## Мета роботи 
Оволодіти концепцією наслідування класів.

## Хід роботи
1. Створено [програму](inheritance.py) з базовим класом `Tree`;
2. Створено дочірній клас `FruitTree`:
- Успадковано функціонал від `Tree` через *super().__init__()*
- Додано нові атрибути: *fruit_type* (тип плодів), *yield_per_year* (урожайність)
- Перевизначено метод *describe()* для виведення додаткової інформації про плоди
- Додано новий метод *harvest()* (унікальний для фруктових дерев)
3. Створено дочірній клас `ForestTree`:
- Успадковано від `Tree` з додаванням атрибуту *wood_type* (тип деревини)
- Перевизначено метод *grow()* зі зміненою швидкістю росту (+0.3м на рік)
4. Продемонстровано роботу ієрархії класів:
```python
apple_tree = FruitTree("Яблуня", 5, 2.5, "яблука", 50)
oak = ForestTree("Дуб", 10, 5.0, "тверда")
```
5. Показано різницю між викликами методів батьківського та дочірніх класів;
6. Продемонстровано принцип "is-a" (яблуня є деревом, дуб є деревом);
6. Результати лабораторної роботи опубліковано у хмарному репозиторії [GitHub](https://github.com/xsp1ke83/oop-it-2025/tree/master/TertishniySergii).

## Висновки: 
У ході виконання лабораторної роботи було успішно досліджено та застосовано принципи наслідування в об'єктно-орієнтованому програмуванні.
