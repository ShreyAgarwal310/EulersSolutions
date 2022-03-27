e = [2,]
i = 1

while(len(e) < 100):
    e.extend([1, 2 * i, 1])
    i += 1

numerator = 1
denominator = e.pop()

for i in e[::-1]:
    denominator, numerator =  (denominator * i + numerator, denominator)

print(sum([int(digit) for digit in str(denominator)]))