## Міністерство освіти і науки України

## Львівського національного університету ветеринарної медицини та біотехнологій імені С.З. Ґжицького
 
# Звіт
### про виконання лабораторної роботи з дисципліни Об'єктно-орієнтоване програмування №13 на тему "Поведінкові шаблони проєктування"
Виконав студент групи ІТ-32

Прийняв доц. Н. Заплатинський
### Львів 2025

## Мета роботи
Мета роботи - познайомитися з групою поведінкових шаблонів проєктування.

## Хід роботи
1. Створив C# [проект](./StructuralPatterns/) в якому реалізував поведінковий шаблон Iterator на основі структури Зв'язаний список. 
Патерн Ітератор (`Iterator Pattern`) — це поведінковий шаблон проєктування, який дозволяє послідовно перебирати елементи колекції без розкриття її внутрішньої структури.
Мета патерну - Розділити інтерфейс доступу до елементів колекції та реалізацію самої колекції, щоб спростити навігацію по елементах.

2. Структура:

`IEnumerator` - (`Iterator`)  -   Інтерфейс, що оголошує методи для ітерації (наприклад, `MoveNext()`, `Current`, `Reset()`, проте не реалізує їх, а дає тільки контракт.)
```csharp
interface IEnumerator<out T> : IEnumerator
    {        
        T Current { get; }
        bool MoveNext();
        void Reset();
    }
```

`LinkedListConcreateIterator` - `(Concrete Iterator)` - Клас який є конкретною реалізацією інтерфейсу `IEnumerator` — знає, як ітерувати по конкретній колекції. 


```csharp
public class LinkedListConcreateIterator<T> : IEnumerator<T>
{
    public int MyProperty { get; set; }
    public T Current => _current.Value;

    object IEnumerator.Current => Current!;
    private LinkedList<T> _head;
    private LinkedList<T> _current;

    public LinkedListConcreateIterator(LinkedList<T> head)
    {
        _head = head;
        _current = _head;        
    }

    public void Dispose()
    {
    }
    public bool _firstTime = true;
    public bool MoveNext()
    {
        // skip the first time        
        if (!_firstTime)    // if not for the first time 
        {
            _current = _current?.Next!;

            if (_current is null)
                return false;

        }
        _firstTime = false;

        return _current != null;

    }

    public void Reset()
    {
        _current = _head;
    }
}

```

`Agregator` - `IEnumerable`   Інтерфейс, який створює ітератор (`GetEnumerator()`)
```csharp
public interface IEnumerable<out T> : IEnumerable
    {
        
        //     Returns an enumerator that iterates through the collection.
        IEnumerator<T> GetEnumerator();
    }    
```
`Concrete Agregator` - Сама колекція (наприклад, масив, список або звязаний список), яка реалізує `Aggregate`
```csharp
public class LinkedList<T>  : IEnumerable<T>
{
    public T Value;
    public LinkedList<T>? Next;
    public LinkedList<T>? Previous;

    public LinkedList(T Value)
    {
        this.Value = Value;
    }

    public IEnumerator<T> GetEnumerator()
    {
        return new LinkedListConcreateIterator<T>(this);
    }

    IEnumerator IEnumerable.GetEnumerator()
    {
        return GetEnumerator();
    }
}
```


## Висновки
Здобув навчиок створення dotnet проектів в VS Code. В ході роботи я реалізував поведінковий шаблон Iterator на мові програмуванні C#. 


