def sieve(n):
	isPrime = [True]*n
	isPrime[0] = False
	isPrime[1] = False
	isPrime[2] = True
	for i in range(3, int(n ** 0.5 + 1), 2):
		index = i * 2
		while(index < n):
			isPrime[index] = False
			index = index + i
	prime = [2]
	for i in range(3,n,2):
		if(isPrime[i]):
			prime.append(i)
	return prime

primes = sieve(100000000)

counter = 0

for i in primes:
	flag = True
	number = i / 10
	while number:
		if ((number % 10) % 2 == 0 or (number % 10) % 5 == 0):
			flag = False
			break
		number //= 10
	if(flag):
		length = len(str(i))
		number = i
		counter += 1
		for j in range(length):
			number = (number % 10) * 10 ** (length - 1) + number // 10
			if(number not in primes):
				counter -= 1
				break

print(counter)