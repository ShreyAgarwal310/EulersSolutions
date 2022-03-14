last = 1001 * 1001
odds = range(1, last + 1, 2)
i = 0
gap = 1
sum = 1

while(odds[i] != last):
    for j in range(4):
        i += gap
        sum += odds[i]
    gap += 1

print(sum)