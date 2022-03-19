import math

def sumOfFactors(n):
    sqrtOfNumber = int(math.sqrt(n))
    sum = 1

    if(n == sqrtOfNumber * sqrtOfNumber):
        sum += sqrtOfNumber
        sqrtOfNumber -= 1
    
    for i in range(2, sqrtOfNumber + 1):
        if (n % i == 0):
            sum = sum + i + (n / i)
    
    return sum

abundant = []

for i in range(12, 28123):
    if (sumOfFactors(i) > i):
        abundant.append(i)

nonAbSum = [x for x in range(28123)]

for i in range(len(abundant)):
    for j in range(i, 28123):
        if(abundant[i] + abundant[j] < 28123):
            nonAbSum[abundant[i] + abundant[j]] = 0
        else:
            break

print(sum(nonAbSum))