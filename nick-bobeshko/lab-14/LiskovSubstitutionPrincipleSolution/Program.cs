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

    class FreeDirectionalVehicle : Vehicle        // буде дозволяти довільний напрямок руху 
    {
        public virtual void Turn() { }   // рух тільки вперед і назад
    }

    class BidirectionalVehicle : Vehicle     // рух тільки вперед і назад
    {
    }

    class Car : FreeDirectionalVehicle
    {
    }

    class Bus : FreeDirectionalVehicle
    {
    }

    class Train : BidirectionalVehicle
    {
        
    }
}
