namespace Lab6
{
    public class CustomerFactory
    {
        public static Customer CreateCustomer(string type)
        {
            if (type.Equals("Mountain"))
            {
                return new MountainCustomer();
            }
            else if (type.Equals("Delinquent"))
            {
                return new DelinquentCustomer();
            }
            else if (type.Equals("Regular"))
            {
                return new RegularCustomer();
            }
            return null;
        }
    }
}