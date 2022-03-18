from itertools import permutations

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

def create(b):
    for i in range(len(b)):
        for j in range(i + 1, len(b)):
            difference = b[j] - b[i]
            if(b[j] + difference in b):
                return str(b[i]) + str(b[j]) + str(b[j] + difference)
    return False

primes = sieve(10000)
primes = [x for x in primes if x > 1487]

for i in primes:
    p = permutations(str(i))
    a = [int(''.join(x)) for x in p]
    a = list(set([x for x in a if x in primes]))
    a.sort()
    if(len(a) >= 3):
        if create(a):
            print(create(a))
            break