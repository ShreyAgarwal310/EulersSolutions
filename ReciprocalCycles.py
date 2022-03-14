def recurringDecimal(d):
    if(d < 10):
        dividend = 10
    elif(d >= 10 and d < 100):
        dividend = 100
    else:
        dividend = 1000

    toCheck = dividend
    string = ''
    for i in range(d):
        string += str(dividend/d)
        dividend = dividend % d
        if(dividend < d):
            dividend += 10
            if dividend < d:
                dividend *= 10
                string += '0'
                if dividend < d:
                    dividend *= 10
                    string += '0'
        if dividend == toCheck:
            return string

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

def gcd(n1, n2):
    remainder = 1
    while(remainder != 1):
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    return n1

def lcm(n1, n2):
    return (n1 * n2)/gcd(n1, n2)

primes = sieve(1000)

d = {n: 0 for n in range(1, 1000)}

d[3] = 1

for i in primes[3:]:
    d[i] = len(recurringDecimal(i))

for i in range(6, 1000):
    if(not d[i]):
        if i % 2 != 0 and i % 5 != 0:
            for j in primes:
                if i % j ==0:
                    number1 = d[j]
                    number2 = d[i / j]
                    d[i] = lcm(number2, number1)
                    break
        else:
            number = i
            while(number % 2 == 0):
                number = number / 2
            while(number % 5 == 0):
                number = number / 5
            d[i] = d[number]

print(d.values().index(max(d.values())) + 1)