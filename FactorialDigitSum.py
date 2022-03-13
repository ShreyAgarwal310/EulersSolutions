from cv2 import FarnebackOpticalFlow_create


num = 100
factorial = 1

for i in range(1, num + 1):
    factorial = factorial * i

print(factorial)

def getSum(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

print(getSum(factorial))