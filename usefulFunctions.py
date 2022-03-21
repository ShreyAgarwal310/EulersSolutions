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

def sieve(n):
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    isPrime[2] = True
    for i in range(3, int(n ** 0.5 + 1), 2):
        index = i * 2
        while(index < n):
            isPrime[index] = False
            index += i
    prime = [2]
    for i in range(3, n, 2):
        if(isPrime[i]):
            prime.append(i)
    return prime

def isPrime(n):
    if(n % 2 == 0):
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if(n % i == 0):
                return False
        return True