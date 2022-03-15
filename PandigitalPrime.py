from itertools import permutations

def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if(n % i == 0):
            return False
    return True

a = '123456789'
flag = True
j = 9

while(flag):
    p = permutations(a[:j])
    p = list(p)[::-1]
    for i in p:
        if(int(i[j - 1]) % 2 != 0):
            number = int(''.join(i))
            if((number + 1) % 6 == 0 or (number - 1) % 6 == 0):
                if(isPrime(number)):
                    print(number)
                    flag = False
                    break
    j -= 1