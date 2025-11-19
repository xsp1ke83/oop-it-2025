## Міністерство освіти і науки України

## Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №14 на тему "Принципи проєктування програмного забезпечення"
Виконав студент групи ІТ-32

Прийняв доц. Н. Заплатинський
### Львів 2025

## Мета роботи
Мета роботи - познайомитися з найбільш поширеними сучасними принципами проєктування програмного забезпечення.

## Хід роботи

Розробив С# проєкт в якому реалізував три SOLID принципи: 
 - Single Responsibility Principle
 - Opened/Closed Principle
 - Liskov Principle

### Принцип єдиного обов’язку (Single Responsibility Principle)
Кожен клас повинен виконувати лише один обов’язок.
Це означає, що всі методи класу мають бути сфокусовані на виконання одного спільного завдання. Якщо є методи, які не відповідають меті існування класу, їх треба винести за його межі.

[SingleResponsibilityPrinciple](./SingleResponsibilityPrincipleSolution/Program.cs):
```csharp
public enum SubscriptionTypes
    {
        Basic,
        Premium
    }

    class User
    {
        public readonly string FirstName;
        public readonly string LastName;
        public readonly string Email;
        public readonly SubscriptionTypes SubscriptionTypes;
        public readonly DateTime SubscriptionExpirationDate;
        public User(string firstName, string lastName, string email, SubscriptionTypes subscriptionTypes, DateTime subscriptionExpirationDate)
        {
            FirstName = firstName;
            LastName = lastName;
            Email = email;
            SubscriptionTypes = subscriptionTypes;
            SubscriptionExpirationDate = subscriptionExpirationDate;
        }

        public override string ToString()
        {
            return $"User First name: {this.FirstName}; Last name: {this.LastName}";
        }

        public bool HasContentAccess()  // ?!!!
        {
            DateTime now = DateTime.Now;

            return (this.SubscriptionTypes == SubscriptionTypes.Premium &&
                    this.SubscriptionExpirationDate.Ticks > now.Ticks);
        }
    }
```
Як бачимо в програмі [SingleResponsibilityPrinciple](./SingleResponsibilityPrinciple/Program.cs) `HasContentAccess()` метод класу `User` виконує бізнес-логіку щодо визначення того чи має користувач доступ до преміум функцій. Що є порушенням принципу Single Responsibility.
Щоб це виправити створимо новий клас `AccessManager`, який буде відповідати за роботу з підписками.



[SingleResponsibilityPrincipleSolution](./SingleResponsibilityPrincipleSolution/Program.cs):
```csharp

    class User
    {
        public readonly string FirstName;
        public readonly string LastName;
        public readonly string Email;
        public readonly SubscriptionTypes SubscriptionTypes;
        public readonly DateTime SubscriptionExpirationDate;
        public User(string firstName, string lastName, string email, SubscriptionTypes subscriptionTypes, DateTime subscriptionExpirationDate)
        {
            FirstName = firstName;
            LastName = lastName;
            Email = email;
            SubscriptionTypes = subscriptionTypes;
            SubscriptionExpirationDate = subscriptionExpirationDate;
        }
        public override string ToString()
        {
            return $"User First name: {this.FirstName}; Last name: {this.LastName}";
        }
    }

    static class AccessManager
    {
        public static bool HasContentAccess(User user)
        {
            DateTime now = DateTime.Now;

            return (user.SubscriptionTypes == SubscriptionTypes.Premium &&
                    user.SubscriptionExpirationDate.Ticks > now.Ticks);
        }
    }
```
### Принцип відкритості/закритості (Open/Close Principle)
Класи мають бути відкриті до розширення, але закриті для змін. 
Якщо є клас, функціонал якого передбачає чимало розгалужень або багато послідовних кроків, і є великий потенціал, що їх кількість буде збільшуватись, то потрібно спроєктувати клас таким чином, щоб нові розгалуження або кроки не призводили до його модифікації.

[OpenClosedPrinciple](./OpenClosedPrinciple/Program.cs):
```csharp
interface IShape
    {
    }

    class Rectangle : IShape
    {
        public readonly int Width;
        public readonly int Height;
        public Rectangle(int width, int height)
        {
            this.Width = width;
            this.Height = height;
        }
    }
    class Square : IShape
    {
        public readonly int Width;
        public Square(int width)
        {
            Width = width;
        }
    }

    class Circle : IShape
    {
        public readonly int Radius;
        public Circle(int radius)
        {
            Radius = radius;
        }
    }

    static class ShapeManager
    {
        public static double GetMaxAreaFromShapes(params IShape[] shapes)     // додавання нових фігур буде призводити до модифікації класу ShapeManager
        {
            IEnumerable<double> areas = shapes.Select((IShape shape) =>
            {
                int area = 0;
                if (shape is Rectangle)
                {
                    Rectangle rect = (Rectangle)shape;
                    return rect.Height * rect.Width;
                }
                if (shape is Square)
                {
                    Square square = (Square)shape;
                    return Math.Pow(square.Width, 2);
                }
                if (shape is Circle)
                {
                    Circle circle = (Circle)shape;
                    return Math.PI * Math.Pow(circle.Radius, 2);
                }
                throw new Exception("Type is not implremented");
            });

            return areas.Max();
        }
    }
```
Як ми бачемо по методу `GetMaxAreaFromShapes` класу `ShapeManager`, кожен раз при додаванні нової фігури ми повинні модифікувати логіку методу, що вже є порушенням Opened/Closed принципу.  

Рішення:
додаємо в інтерфейс `IShape` контракт на метод `GetArea()` щоб кожна фігура реалізувала його.


[SingleResponsibilityPrincipleSolution](./OpenClosedPrincipleSolution/Program.cs):
```csharp
interface IShape
    {
        double GetArea();
    }

    class Rectangle : IShape
    {
        public readonly int Width;
        public readonly int Height;
        public Rectangle(int width, int height)
        {
            this.Width = width;
            this.Height = height;
        }

        public double GetArea()
        {
            return this.Height * this.Width;
        }
    }
    class Square : IShape
    {
        public readonly int Width;
        public Square(int width)
        {
            Width = width;
        }

        public double GetArea()
        {
            return Math.Pow(this.Width, 2);
        }
    }

    class Circle : IShape
    {
        public readonly int Radius;
        public Circle(int radius)
        {
            Radius = radius;
        }

        public double GetArea()
        {
            return Math.PI * Math.Pow(this.Radius, 2);
        }
    }

    static class ShapeManager
    {
        public static double GetMaxAreaFromShapes(params IShape[] shapes)
        {
            IEnumerable<double> areas = shapes.Select((IShape shape) => shape.GetArea());

            return areas.Max();
        }
    }
```
Таким чином, при додаванні нової фігури нам не потрібно модифікувати метод 



### Принцип підстановки Лісков (Liskov Substitution Principle)

Якщо об’єкт базового класу замінити об’єктом його похідного класу, то програма має продовжувати працювати коректно. Поведінка підкласу не повинна порушувати логіку базового класу.

Приклад: 

[LiskovSubstitutionPrinciple](./LiskovSubstitutionPrinciple/Program.cs):
```csharp
class Vehicle
    {
        public virtual void Accelerate()
        { }
        public virtual void Slowdown() { }
        public virtual void Turn() { }
    }

    class Car : Vehicle
    {
        public virtual void Accelerate() { }
        public virtual void Slowdown() { }
        public virtual void Turn() { }
    }
    class Bus : Vehicle
    {
        public override void Slowdown()
        {
            base.Slowdown();
            // do something..
        }
    }
```
Все буде працювати до того моменту, допоки ми не вирішимо додати клас Поїзд:
```csharp
    class Train : Vehicle
    {
        public override void Turn()
        {            
        }
    }
```
Оскільки поїзд не може змінювати довільно напрямок свого руху, то turn батьківського класу буде порушувати принцип підстановки Лісков.

Щоб виправити цю ситуацію, ми можемо додати два батьківські класи: `FreeDirectionalVehicle` — який буде дозволяти довільний напрямок руху і `BidirectionalVehicle` — рух тільки вперед і назад. Тепер всі класи будуть наслідувати тільки ті методи, які можуть забезпечити.

[LiskovSubstitutionPrincipleSolution](./LiskovSubstitutionPrincipleSolution/Program.cs):
```csharp
class Car : FreeDirectionalVehicle
    {
    }

    class Bus : FreeDirectionalVehicle
    {
    }

    class Train : BidirectionalVehicle
    {        
    }
```

## Висновки
Розглянув три правила проектування SOLID, що допомагають робити код більш гнучким та легким у підтримці та розширенні.