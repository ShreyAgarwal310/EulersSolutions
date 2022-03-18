def numFactors(n):
    i = 2
    a = set()
    while(i < n ** 0.5 or n == 1):
        if(n % i == 0):
            n /= i
            a.add(i)
            i -= 1
        i += 1
    return(len(a) + 1)

j = 2 * 3 * 5 * 7

while True:
    if(numFactors(j) == 4):
        j += 1
        if(numFactors(j) == 4):
            j += 1
            if(numFactors(j) == 4):
                j += 1
                if(numFactors(j) == 4):
                    print(j - 3)
                    break
    j += 1