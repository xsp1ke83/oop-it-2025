using System.Collections;

namespace StructuralPatterns;

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
