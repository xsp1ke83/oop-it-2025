using AdapterObjectLevel.AdapteeImpl;

namespace AdapterObjectLevel;

class Adapter : Target
{
    private Adaptee _adaptee = new Adaptee();
    public override void Request()
    {
        _adaptee.SpecificRequest();
    }
}
