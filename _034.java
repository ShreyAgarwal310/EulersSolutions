public class _034
{
    public static int factorial(int n)
    {
        int fact = 1;
        for(int i = 1; i <= n; i++)
        {
            fact *= i;
        }

        return fact;
    }

    public static void main(String[] args)
    {
        int sum = 0;

        for(int i = 10; i <= 2540161; i++)
        {
            int sumOfFact = 0;
            int number = i;

            while(number > 0)
            {
                int d = number % 10;
                number /= 10;
                sumOfFact += factorial(d);
            }

            if(sumOfFact == i)
            {
                sum += i;
            }
        }

        System.out.println(sum);
    }
}