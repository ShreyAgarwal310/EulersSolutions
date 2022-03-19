public class _012
{
    private static int NumberOfDivisors(int num)
    {
        int numDivisors = 0;
        int sqrt = (int)Math.sqrt(num);

        for(int i = 1; i <= sqrt; i++)
        {
            if(num % i == 0)
            {
                numDivisors += 2;
            }
        }

        if(sqrt*sqrt == num)
        {
            numDivisors--;
        }

        return numDivisors;
    }

    public static void main(String[] args)
    {
        int number = 0;
        int i = 1;

        while(NumberOfDivisors(number) < 500)
        {
            number += i;
            i++;
        }

        System.out.print(number);
    }
}
