namespace LiskovSubstitutionPrinciple
{
    internal class Program
    {
        static void Main(string[] args)
        {

        }
    }

    class Vehicle
    {
        public virtual void Accelerate()
        { }
        public virtual void Slowdown() { }
        public virtual void Turn() { }
    }

    class Car : Vehicle
    {
        //public virtual void Accelerate() { }
        //public virtual void Slowdown() { }
        //public virtual void Turn() { }
    }
    class Bus : Vehicle
    {
        public override void Slowdown()
        {
            base.Slowdown();
            // do something..
        }
    }
    class Train : Vehicle
    {
        public override void Turn()
        {
            throw new NotSupportedException();
        }
    }

}
