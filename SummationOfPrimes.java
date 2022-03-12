public class SummationOfPrimes 
{
    private static boolean is_prime(long num)
    {
        int count = 0;
        long sqrt = (long) Math.sqrt(num);

        for(long i = 1; i <= sqrt; i++)
        {
            if(num % i == 0)
            {
                count++;
            }
            if(count > 1)
            {
                return false;
            }
        }

        return true;
    }
    
    public static void main(String[] args)
    {
        long sum = 0;
        for(long i = 2; i < 2000000; i++)
        {
            if(is_prime(i))
            {
                sum += i;
            }
        }

        System.out.print(sum);
    }
}
