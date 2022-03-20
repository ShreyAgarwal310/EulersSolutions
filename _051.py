wildcards = []
primes = []
primes.append(2)
searched = set()

def genWildcardStrings(s, index):
    if(index > 0 and s not in searched):
        wildcards.append(s)
        searched.add(s)
    for x in range(index, len(s)):
        genWildcardStrings(createPlaceholder(s, x), x+1)

def createPlaceholder(s, index):
    return s[0:index] + '*' + s[index+1:]

def binarySearch(prime):
    start = 0
    end = len(primes)
    middle = int((end + start)/2)
    
    while(start < end 
          and primes[middle] != prime 
          and middle < len(primes)):
        if(primes[middle] < prime):
            start = middle+1
        else:
            end = middle-1
        middle = int((end + start)/2)
    
    if(middle < len(primes) and primes[middle] == prime):
        return middle
    else:
        return -1

for x in range(3, 1000000):
    found = False
    for i in range(0, len(primes)):
        if(x % primes[i] == 0):
            found = True
            break
        if(primes[i] * primes[i] > x):
            break
    if not found:
        primes.append(x)

for x in range(0, len(primes)):
    wildcards = []
    genWildcardStrings(str(primes[x]), 0)
    for y in range(1, len(wildcards)):
        count = 0
        for z in range(0, 10):
            num = int(wildcards[y].replace('*', str(z)))
            if(len(str(num)) < len(wildcards[y])):
                continue
            if(binarySearch(num) >= 0):
                count += 1
        if count >= 8:
            print(wildcards[y])
            exit(0)