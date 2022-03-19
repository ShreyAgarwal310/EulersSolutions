public class _006 {
    public static void main(String[] args)
    {
        int n = 100;
        int sum = 0;
        int sumOfSquares = 0;
        int squareOfSum;

        for(int i = 1; i <= n; i++)
        {
            sum += i;
            sumOfSquares += i*i;
        }

        squareOfSum = sum*sum;

        System.out.print("The difference between the sum of the squares and the square of the sums is " + (squareOfSum-sumOfSquares));
    }
}