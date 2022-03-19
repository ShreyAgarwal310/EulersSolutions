from collections import Counter

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

primes = [x for x in primes if len(str(x)) - len(set(str(x))) >= 3]

def pdr(n):
    n = str(n)
    sol = []

    for dupe in (Counter(n) - Counter(set(n))):
        a = ['1', '2', '3', '4', '5', '6' '7', '8', '9']
        temp = [int(n.replace(dupe, x)) for x in a]
        sol.append(temp)

    return temp

checked = []

def check(l):
    for i in l:
        checked.append(i)
        if(i not in primes):
            l.remove(i)
    return l

flag = True
i = 0

while(flag):
    if(primes[i] not in checked):
        replacements = pdr(primes[i])
        for j in replacements:
            if(len(check(j)) == 8):
                print(j[0])
                flag = False
                break

    i += 1