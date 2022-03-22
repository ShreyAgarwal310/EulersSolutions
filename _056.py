from usefulFunctions import sumOfDigits

largest = 0

for a in range(1, 100):
    for b in range(0, 100):
        sum = sumOfDigits(a ** b)
        if(sum > largest):
            largest = sum

print(largest)