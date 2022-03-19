import math

def isPrime(n):
    if(n % 2 == 0):
        return False
    else:
        for i in range(3, int(n ** 0.5 + 1), 2):
            if(n % i == 0):
                return False
        return True

num = 3

primes = [2]

while(True):
    if(isPrime(num)):
        primes.append(num)
    else:
        for i in primes:
            if(math.sqrt(((num - i) / 2)) == int(math.sqrt(((num - i) / 2)))):
                break
        else:
            print(num)
            break
    num += 2