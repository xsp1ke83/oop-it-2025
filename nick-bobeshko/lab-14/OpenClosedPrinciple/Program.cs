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
                throw new Exception("Type is not implremented");    // even if one type is not implemented throw an error
            });

            return areas.Max();
        }
    }
}
