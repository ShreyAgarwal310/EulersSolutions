import math
from usefulFunctions import sieve, millerRabin

def comb(a, b):
    lenA = math.floor(math.log10(a)) + 1
    lenB = math.floor(math.log10(b)) + 1
    if(millerRabin(int(a * (10 ** lenB) + b)) and millerRabin(int(b * 10 ** lenA) + a)):
        return True
    
    return False

primes = sieve(10000)

for a in primes:
    for b in primes:
        if(b < a):
            continue
        if(comb(a, b)):
            for c in primes:
                if(c < b):
                    continue
                if(comb(a, c) and comb(b, c)):
                    for d in primes:
                        if(d < c):
                            continue
                        if(comb(a, d) and comb(b, d) and comb(c, d)):
                            for e in primes:
                                if(e < d):
                                    continue
                                if(comb(a, e) and comb(b, e) and comb(c, e) and comb(d, e)):
                                    print(a + b + c + d + e)