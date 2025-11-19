namespace LiskovSubstitutionPrincipleSolution
{
    internal class Program
    {
        static void Main(string[] args)
        {
        }
    }

    class Vehicle
    {
        public virtual void Accelerate() { }
        public virtual void Slowdown() { }
    }

    class FreeDirectionalVihicle : Vehicle        // буде дозволяти довільний напрямок руху 
    {
        public virtual void Turn() { }   // рух тільки вперед і назад
    }

    class BidirectionalVehicle : Vehicle     // рух тільки вперед і назад
    {
    }

    class Car : FreeDirectionalVihicle
    {
    }

    class Bus : FreeDirectionalVihicle
    {
    }

    class Train : BidirectionalVehicle
    {
        
    }
}
