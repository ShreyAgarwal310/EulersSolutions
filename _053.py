from math import factorial as f

counter = 0

def nCr(n, r):
    return (f(n)/(f(r) * f(n - r)))

for n in range(23, 101):
    for r in range(4, n - 3):
        if(nCr(n, r) > 1000000):
            counter += 1

print(counter)