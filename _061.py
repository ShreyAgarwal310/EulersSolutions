triangle = []
square = []
pentagonal = []
hexagonal = []
heptagonal = []
octagonal = []

for n in range(45, 141):
    i = n * (n + 1) / 2
    triangle.append(i)

for n in range(32, 100):
    i = n ** 2
    square.append(i)

for n in range(26, 82):
    i = n * (3 * n - 1) / 2
    pentagonal.append(i)

for n in range(23, 71):
    i = n * (2 * n - 1)
    hexagonal.append(i)

for n in range(21, 64):
    i = n * (5 * n - 3) / 2
    heptagonal.append(i)

for n in range(19, 59):
    i = n * (3 * n - 2)
    octagonal.append(i)