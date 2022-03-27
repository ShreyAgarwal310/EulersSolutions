from math import sqrt

def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convergents = [a0]
    period = 0
    if(a0 != sqrt(n)):
        while(an != 2 * a0):
            mn = dn * an - mn
            dn = (n - mn ** 2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

def cf_inv(cf):
    numerator = 1
    denominator = cf.pop()
    while(cf):
        denominator, numerator = denominator * cf.pop() + numerator, denominator
    return denominator, numerator

largest = 0, 0

for i in range(1, 1001):
    if(i % sqrt(i) != 0):
        continued_fraction = cf(i)
        if(len(continued_fraction) % 2 != 0):
            u, v = cf_inv(continued_fraction)
            u, v = 2*u**2+1, 2*u*v
        else:
            u, v = cf_inv(continued_fraction)
        if(u > largest[1]):
            largest = i, u

print(largest[0])