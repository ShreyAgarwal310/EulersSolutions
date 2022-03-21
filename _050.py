from usefulFunctions import sieve

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