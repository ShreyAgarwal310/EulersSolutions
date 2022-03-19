sequence = [0, 1]
term = 2

while True:
    next = sequence[term - 1] + sequence[term - 2]
    sequence.append(next)
    if(next > 10 ** 999):
        print(term)
        break
    
    term += 1