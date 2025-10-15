namespace StructuralPatterns;


class Program
{
    static void Main(string[] args)
    {
        
        Console.ReadLine();
        Console.WriteLine("Hello, World From Linux!");

        int length = 10;
        LinkedList<int> head = new LinkedList<int>(99);     // first value

        LinkedList<int> linkedList = head;
        for (int i = 0; i < length; i++)
        {
            var newLinkedList = new LinkedList<int>(i);
            newLinkedList.Previous = linkedList;
            linkedList.Next = newLinkedList;

            linkedList = newLinkedList;
        }


        Console.WriteLine("Loop over all the nodes using <for> (starting with Head): ");

        LinkedList<int> linkNode = head;
        
        
        while (linkNode is not null)
        {
            Console.WriteLine(linkNode.Value);
            linkNode = linkNode.Next!;
        }

        Console.WriteLine("Loop over all the nodes using <foreach> (starting with Head): ");

        // IEnumerator<int> iEnum = head.GetEnumerator();
        // while (iEnum.MoveNext() is not false)
        // {
        //     Console.WriteLine(iEnum.Current);
        // }

        foreach (int item in head)
        {
            Console.WriteLine(item);
        }

    }
}
