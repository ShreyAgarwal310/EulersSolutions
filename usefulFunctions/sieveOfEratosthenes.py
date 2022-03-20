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