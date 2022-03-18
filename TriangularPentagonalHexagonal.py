def isPentagon(n):
    if((1 + (24 * n + 1) ** 0.5) % 6 == 0):
        return True
    return False

def isHexagonal(n):
    if((1 + (8 * n + 1) ** 0.5) % 4 == 0):
        return True
    return False

i = 286

while True:
    triangle = i * (i + 1) / 2
    if(isPentagon(triangle) and isHexagonal(triangle)):
        print(int(triangle))
        break
    i += 1