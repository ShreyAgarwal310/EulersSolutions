p = 1
q = 1
counter = 0

for i in range(1000):
    a1 = p + 2 * q
    b1 = p + q
    if(len(str(a1)) > len(str(b1))):
        counter += 1
    p = a1
    q = b1

print(counter)