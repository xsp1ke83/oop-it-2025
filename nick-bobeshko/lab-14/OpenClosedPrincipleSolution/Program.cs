namespace OpenClosedPrinciple
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Rectangle rectangle = new Rectangle(100, 120);
            Square square = new Square(100);
            Circle circle = new Circle(400);

            double max = ShapeManager.GetMaxAreaFromShapes(rectangle, square, circle);
            Console.WriteLine(max);
        }
    }

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
}
