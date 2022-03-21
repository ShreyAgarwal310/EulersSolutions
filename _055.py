def isLychrel(n):
    for i in range(50):
        num = n + int(str(n)[::-1])
        if(str(num) == str(num)[::-1]):
            return False
        n = num
    
    return True

counter = 0

for i in range(10001):
    if(isLychrel(i)):
        counter += 1

print(counter)