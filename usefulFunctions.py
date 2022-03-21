import math
import random

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

def millerRabin(n, k = 3):
    if(n < 6):
        return [False, False, True, True, False, True][n]
    elif(n % 2 == 0):
        return False
    else:
        s, d = 0, n - 1
        while(d % 2 == 0):
            s, d = s + 1, d >> 1
        for a in random.sample(range(2, n - 2), k):
            x = pow(a, d, n)
        if(x != 1 and x + 1 != n):
            for r in range(1, s):
                x = pow(x, 2, n)
                if(x == 1):
                    return False
                elif(x == n - 1):
                    a = 0
                    break
            if(a):
                return False 
        return True

def sumOfDigits(n):
    sum = 0
    while(n != 0):
        sum += n % 10
        n //= 10
    
    return sum