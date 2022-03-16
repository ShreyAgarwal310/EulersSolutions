import math

def isPrime(n):
    sqrt = math.sqrt(n)
    for i in range(int(n), int(sqrt + 1)):
        if(n % i == 0):
            return False
    return True

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

aMax = 0
bMax = 0
nMax = 0

primes = sieve(87400)

for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while(isPrime(abs(n * n + a * n + b))):
            n += 1
        if(n > nMax):
            aMax = a
            bMax = b
            nMax = n

print(n)