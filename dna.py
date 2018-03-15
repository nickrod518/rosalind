aCount = 0
cCount = 0
gCount = 0
tCount = 0

for c in input():
    if c == "A":
        aCount += 1
    elif c == "C":
        cCount += 1
    elif c == "G":
        gCount += 1
    elif c == "T":
        tCount += 1

print(aCount, cCount, gCount, tCount)
