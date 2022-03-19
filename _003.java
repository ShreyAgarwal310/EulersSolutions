import java.util.Scanner;

public class _003
{
    public static void main(String[] args)
    {
        try (Scanner input = new Scanner(System.in)) {
            System.out.print("Enter i Value: ");
            long n = input.nextLong();
            long number = n;
            long largestPrimeFactor = n;
            long i = 2;
            while (i <= n && n != 1) 
            {
                if (n % i == 0) 
                {
                    n = n / i;
                    largestPrimeFactor = i;
                }
                else 
                {
                    i = i + 1;
                }
            }
            System.out.println("The largest prime factor of the number "+ number + " is "+ largestPrimeFactor);
        }
    }
}