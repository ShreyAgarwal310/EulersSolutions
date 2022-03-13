with open('MaximumPathSumII.txt') as file:
    pyramid = file.read()

print(pyramid)

number = pyramid.strip().split('\n')

for i in range(1, len(number)):
    number[i] = number[i].strip().split(' ')
    number[i] = [int(x) for x in number[i]]

number[0] = [59]

counter = 0

for i in range(len(number) - 2, -1, -1):
	for j in range(len(number[i])):
		number[i][j] = number[i][j] + max(number[i + 1][j], number[i + 1][j + 1])
		counter += 1
	number.pop()

print(number)