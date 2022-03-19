a = ''

for i in range(1, 185186):
    a += str(i)

d1 = int(a[0])
d10 = int(a[9])
d100 = int(a[99])
d1000 = int(a[999])
d10000 = int(a[9999])
d100000 = int(a[99999])
d1000000 = int(a[999999])

print(d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000)