import random
digitcount = random.randint(5,10)

binarr = []
for i in range(0,digitcount):
    binarr = binarr + [random.randint(0,1)]
binarr = list(reversed(binarr))
print(digitcount,'\n',binarr,'\n')

finaldec = 0
y=0
for x in binarr:
    if x == 1:
        finaldec = finaldec + 2**y
        y = y+1

    if x==0:
        y=y+1

print(finaldec)
