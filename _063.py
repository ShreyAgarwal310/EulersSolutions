from math import log10

count = 0

for i in range(1, 10):
    count += int(1 / (1 - log10(i)))

print(count)