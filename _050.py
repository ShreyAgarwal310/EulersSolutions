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

primes = sieve(1000000)
length = 0
largest = 0
lastj = len(primes)

for i in range(len(primes)):
    for j in range(i + length, lastj):
        sol = sum(primes[i:j])
        if(sol < 1000000):
            if(sol in primes):
                length = j - i
                largest = sol
        else:
            lastj = j + 1
            break

print(largest)