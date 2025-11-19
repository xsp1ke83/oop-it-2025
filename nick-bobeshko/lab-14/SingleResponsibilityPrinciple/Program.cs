using System.Net.Http.Headers;
using System.Security.Cryptography.X509Certificates;

namespace SingleResponsibilityPrinciple
{
    internal class Program
    {
        static void Main()
        {
            User user1 = new User(
                "Nicolas", 
                "Jonson", 
                "afwenicolas@firstmail.com", 
                SubscriptionTypes.Premium,
                new DateTime(2026, 1, 1));

            //Console.WriteLine(user1.HasContentAccess());
        }
    }
    public enum SubscriptionTypes
    {
        Basic,
        Premium
    }

    /// <summary>
    /// Клас User - Його обов’язок надавати інформацію про користувача: ім’я, email і тип підписки, яку він використовує в сервісі
    /// </summary>
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

        public bool HasContentAccess()  // ?!!!
        {
            DateTime now = DateTime.Now;

            return (this.SubscriptionTypes == SubscriptionTypes.Premium &&
                    this.SubscriptionExpirationDate.Ticks > now.Ticks);
        }
    }

}
