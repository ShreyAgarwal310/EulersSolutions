solution = 0

for i in range(1, 1001):
    solution += i ** i

print(str(solution)[-10:])