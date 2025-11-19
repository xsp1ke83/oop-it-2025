namespace SingleResponsibilityPrincipleSolution
{
    internal class Program
    {
        static void Main()
        {
            User user1 = new User(
                "Michael",
                "Miers",
                "michael_miers@firstmail.com",
                SubscriptionTypes.Premium,
                new DateTime(2024, 1, 1));

            Console.WriteLine(AccessManager.HasContentAccess(user1));
        }
    }
    public enum SubscriptionTypes
    {
        Basic,
        Premium
    }
    class User
    {
        public readonly string FirstName;
        public readonly string LastName;
        public readonly string Email;
        public readonly SubscriptionTypes SubscriptionTypes;
        public readonly DateTime SubscriptionExpirationDate;
        public User(string firstName, string lastName, string email, SubscriptionTypes subscriptionTypes, DateTime subscriptionExpirationDate)
        {
            FirstName = firstName;
            LastName = lastName;
            Email = email;
            SubscriptionTypes = subscriptionTypes;
            SubscriptionExpirationDate = subscriptionExpirationDate;
        }
        public override string ToString()
        {
            return $"User First name: {this.FirstName}; Last name: {this.LastName}";
        }
    }

    static class AccessManager
    {
        public static bool HasContentAccess(User user)
        {
            DateTime now = DateTime.Now;

            return (user.SubscriptionTypes == SubscriptionTypes.Premium &&
                    user.SubscriptionExpirationDate.Ticks > now.Ticks);
        }
    }
}