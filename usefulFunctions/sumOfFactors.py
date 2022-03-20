import math

def sumOfFactors(n):
    sqrtOfNumber = int(math.sqrt(n))
    sum = 1

    if(n == sqrtOfNumber * sqrtOfNumber):
        sum += sqrtOfNumber
        sqrtOfNumber -= 1
    
    for i in range(2, sqrtOfNumber + 1):
        if (n % i == 0):
            sum = sum + i + (n / i)
    
    return sum