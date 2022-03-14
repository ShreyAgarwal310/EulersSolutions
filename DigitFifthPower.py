sum = 0

for i in range(2, 5 * 9 ** 5 + 1):
	if sum([int(x) ** 5 for x in str(i)]) == i:
		sum += i

print(sum)