public class _021
{
    private static int sumOfFactors(int number) {
        int sqrtOfNumber = (int) Math.sqrt(number);
        int sum = 1;
     
        if (number == sqrtOfNumber * sqrtOfNumber)
        {
            sum += sqrtOfNumber;
            sqrtOfNumber--;
        }
     
        for (int i = 2; i <= sqrtOfNumber; i++)
        {
            if (number % i == 0)
            {
                sum = sum + i + (number / i);
            }
        }
        return sum;
    }
    
    public static void main(String[] args)
    {
        int sumAmicible = 0;
        int factorsi, factorsj;
        
        for (int i = 2; i <= 10000; i++) {
            factorsi = sumOfFactors(i);
            if (factorsi > i && factorsi <= 10000) {
                factorsj = sumOfFactors(factorsi);
                if (factorsj == i) {
                    sumAmicible += i + factorsi;
                }
            }
        }

        System.out.println(sumAmicible);
    }
}