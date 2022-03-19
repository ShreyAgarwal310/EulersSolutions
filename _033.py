from fractions import Fraction

product = 1

for i in range(10, 100):
    for j in range(i + 1, 100):
        common = list(set(str(i)) & set(str(j)))

        if(len(common) != 0):
            if(common[0] != '0'):
                num = list(str(i))
                den = list(str(j))

                num.remove(common[0])
                den.remove(common[0])

                if(num != '0' and den[0] != '0'):
                    if(Fraction(int(num[0]), int(den[0])) == Fraction(i, j)):
                        product *= Fraction(i, j)

print(product.denominator)