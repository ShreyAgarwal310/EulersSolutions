from collections import Counter

def highCard(hand):
    highest = 0
    for i in hand:
        if(i == "A"):
            return 14
        elif(i == "K"):
            if(13 >= highest):
                highest = 13
        elif(i == "Q"):
            if(12 >= highest):
                highest = 12
        elif(i == "J"):
            if(11 >= highest):
                highest = 11
        elif(i == "T"):
            if(10 >= highest):
                highest = 10
        elif(int(i) > highest):
            highest = int(i)
    
    return highest

def convertToLists(s):
    cards = s.split()
    cardValue = []
    cardType = []

    for i in cards:
        cardValue.append(i[0])
        cardType.append(i[1])
    
    return [cardValue, cardType]

def numPairs(l):
    count = Counter(l) - Counter(set(l))
    pairs = 0

    for i in count:
        if(count[i] == 1):
            pairs += 1
    if(pairs):
        return pairs + 1
    
    return 0

def threeOfAKind(l):
    count = Counter(l) - Counter(set(l))

    for i in count:
        if(count[i] == 2):
            return 4
    
    return 0

def straight(l):
    rating = {14: 'A', 13: 'K', 12: 'Q', 11: 'J', 10: 'T', 9: '9', 8: '8', 7: '7', 6: '6', 5: '5', 4: '4', 3: '3', 2: '2', 1: '1'}
    high = highCard(l)

    if(rating[high - 1] in l):
        if(rating[high - 2] in l):
            if(rating[high - 3] in l):
                if(rating[high - 4] in l):
                    return 5
    
    return 0

def flush(l):
    if(len(set(l)) == 1):
        return 6
    
    return 0

def fullHouse(l):
    if(threeOfAKind(l)):
        if(numPairs(l) == 2):
            return 7
    
    return 0

def fourOfAKind(l):
    dupes = Counter(l) - Counter(set(l))

    for i in dupes:
        if(dupes[i] == 3):
            return 8

    return 8

def straightFlush(l, v):
    if(straight(l) and flush(v)):
        return 9

    return 0

def royalFlush(l, v):
    if(set(['T', 'J', 'Q', 'K', 'A']) == set(l)):
        if(len(set(v)) == 1):
            return 10

    return 0

def pairedNumber(l):
    repeated = (Counter(l) - Counter(set(l))).keys()
    rating = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, '1': 1}
    highest = 0

    for i in repeated:
        if(rating[i] > highest):
            highest = rating[i]
    
    return highest

f = open('_054.txt')
games = f.read()
f.close

twoHands = games.strip().split('\n')

hands = []

for i in twoHands:
    fh = convertToLists(i[:14])
    sh = convertToLists(i[15:])
    hands.append([fh, sh])

player1 = 0

for i in hands:
    p1v = i[0][0]
    p2v = i[1][0]
    p1s = i[0][1]
    p2s = i[1][1]
    p1 = 0
    p2 = 0

    flag = False

    if(numPairs(p1v)):
        p1 = numPairs(p1v)
        flag = True
    if(threeOfAKind(p1v)):
        p1 = threeOfAKind(p1v)
        flag = True
    if(straight(p1v)):
        p1 = straight(p1v)
    if(flush(p1s)):
        p1 = flush(p1s)
    if(fullHouse(p1v)):
        p1 = fullHouse(p1v)
        flag = True
    if(fourOfAKind(p1v)):
        p1 = fourOfAKind(p1v)
        flag = True
    if(straightFlush(p1v, p1s)):
        p1 = straightFlush(p1v, p1s)
    if(royalFlush(p1v, p1s)):
        p1 = royalFlush(p1v, p1s)
    
    if(numPairs(p2v)):
        p2 = numPairs(p2v)
        flag = True
    if(threeOfAKind(p2v)):
        p2 = threeOfAKind(p2v)
        flag = True
    if(straight(p2v)):
        p2 = straight(p2v)
    if(flush(p2s)):
        p2 = flush(p2s)
    if(fullHouse(p2v)):
        p2 = fullHouse(p2v)
        flag = True
    if(fourOfAKind(p2v)):
        p2 = fourOfAKind(p2v)
        flg = True
    if(straightFlush(p2v, p2s)):
        p2 = straightFlush(p2v, p2s)
    if(royalFlush(p2v, p2s)):
        p2 = royalFlush(p2v, p2s)

    if(p1 > p2):
        player1 += 1
    elif(p1 == p2):
        if(flag):
            if(pairedNumber(i[0][0]) > pairedNumber(i[1][0])):
                player1 += 1
            elif(pairedNumber(i[0][0]) == pairedNumber(i[1][0])):
                if(highCard(i[0][0]) > highCard(i[1][0])):
                    player1 += 1
        else:
            if(highCard(i[0][0]) > highCard(i[1][0])):
                player1 += 1
    
print(player1)