using System;
using System.Collections;

namespace StructuralPatterns;

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
