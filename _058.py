from usefulFunctions import isPrime

i = 0
gap = 1
ratio = 1
primes = []
allNums = [1]

while(ratio > 0.1):
    for j in range(4):
        i += gap
        currentNum = 2 * i + 1
        allNums.append(currentNum)
        if(isPrime(currentNum)):
            primes.append(2 * i + 1)
    
    ratio = float(len(primes)/len(allNums))
    gap += 1

print((2 * i + 1) ** 0.5)