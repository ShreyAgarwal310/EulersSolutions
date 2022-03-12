public class EvenFibonacciNumbers
{
    public static void main(String[] args) {
        int sum = 0 ;
        int x1 = 1;
        int x2 = 2;
        while (x1 < 4000000) {
            if (x1 % 2 == 0){
                sum += x1;
            }
            x2=x1+x2;
            x1=x2-x1;
        }
        System.out.println(sum);
    }
}
