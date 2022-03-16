def sieve(n):
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int(n ** 0.5 + 1)):
        index = i * 2
        while index < n:
            isPrime[index] = False
            index = index + i

    prime = []

    for i in range(n):
        if isPrime[i] == True:
            prime.append(i)

    return prime

def isPrime(n):
    for i in range(2, int(abs(n) ** 0.5) + 1):
        if(n % i == 0):
            return False

    return True

primes1000 = sieve(1000)

primes = primes1000[:]

largest = 0
axb = 0

for b in primes1000:
    for a in primes1000:
        i = 0
        while True:
            quadratic = i ** 2 + a * i + b
            if(quadratic not in primes):
                if(isPrime(quadratic)):
                    primes.append(quadratic)
                else:
                    if(i - 1 > largest):
                        largest = i - 1
                        axb = a * b
                    break
            i += 1
        i = 0
        while True:
            quadratic = i ** 2 - a * i + b
            if(quadratic not in primes):
                if(isPrime(quadratic) and quadratic > 0):
                    primes.append(quadratic)
                else:
                    if(i - 1 > largest):
                        largest = i - 1
                        axb = -1 * a * b
                    break
            i += 1

print(axb)
