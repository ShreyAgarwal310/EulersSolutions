from functools import reduce

def convert(n):
    if(len(n) == 2):
        return '0' + n
    elif(len(n) == 1):
        return '00' + n
    return n

def multiple(n):
    mn = []
    mul = 1
    i = 1
    while(mul < 1000):
        mul = i * n
        i += 1
        mn.append(mul)
    mn.pop()
    mn = map(str, mn)
    mn = map(convert, mn)

def concat(a, b):
    c = []
    for i in a:
        for j in b:
            if(i[:2] == j[1:] and len(set(j[0] + i)) == len(j[0] + i)):
                c.append(j[0] + 1)
    return c

def missing(n):
    for i in '0123456789':
        if(i not in n):
            return i + n

m17, m13, m11, m7, m5, m3, m2 = (multiple(17), multiple(13), multiple(11), multiple(7), multiple(5), multiple(3), multiple(2))

d = reduce(concat, [m17, m13, m11, m7, m5, m3, m2])
d = map(missing, d)
d = map(int, d)
print(sum(d))