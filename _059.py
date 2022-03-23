f = open("_059.txt", "r")
 
contents = f.readlines()
realContents = []
for x in contents:
    realContents.append(x.split(","))
 
finalContents = []
for x in realContents[0]:
     finalContents.append(int(x))
 
def isAcceptable(myChar):
    return('a' <= myChar <= 'z' or 'A' <= myChar <= 'Z' or myChar == ' ' or myChar == '\'' or myChar == ',' or myChar == '"' or myChar == '[' or myChar == ']' or myChar == ':' or '0' <= myChar <= '9' or myChar == '/' or myChar == '.' or myChar == '(' or myChar == ')' or myChar == ';' or myChar=='+')
    
def solve(cipherText):
     tl = len(cipherText)
     alphabet = "abcdefghijklmnopqrstuvwxyz"
     possible = []
     for a in alphabet:
         for b in alphabet:
             for c in alphabet:
                 myGuess = a + b + c
                 asciiIndices = [ord(a), ord(b), ord(c)]
                 s = ""
                 bad = False
                 for x in range(tl):
                     myChar = chr(cipherText[x] ^ asciiIndices[x % 3])
                     if(not isAcceptable(myChar)):
                         bad = True
                         break
                     s += myChar
                 if(not bad):
                     possible.append(s)
     total = -1
     for x in possible:
         subTotal = 0
         for y in x:
             subTotal += ord(y)
         if(total == -1):
             total = subTotal
     return total
 
print(solve(finalContents))