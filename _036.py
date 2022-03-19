sum = 0

for i in range(1, 1000000, 2):
    if(str(i) == str(i)[::-1]):
        if(bin(i)[2:] == bin(i)[2:][::-1]):
            sum += i

print(sum)