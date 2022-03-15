from math import sqrt

f = open('CodedTriangleNumbers.txt')
words = f.read()
f.close
words = words.strip().split(',')

def convert(char):
    return ord(char) - 64

counter = 0

for word in words:
    x = sum(map(convert, word[1:-1]))
    if(sqrt(8 * x + 1) == int(sqrt(8 * x + 1))):
        counter += 1

print(counter)