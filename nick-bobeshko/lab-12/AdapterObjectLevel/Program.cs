namespace AdapterObjectLevel;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Object Adapter!");

        Target target = new Adapter();
        target.Request();
        
        
    }
}
