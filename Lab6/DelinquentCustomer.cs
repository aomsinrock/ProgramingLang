namespace Lab6
{
    public class DelinquentCustomer : Customer
    {
        public override string CreateMail()
        {
            return "Delinquent Customer";
        }
    }
}