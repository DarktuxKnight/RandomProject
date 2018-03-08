from random import randint
import string

normalnum = randint(100,200)
#normalnum = 113
orignormalsum = normalnum
print(normalnum)

rannumlist = list(str(normalnum))

numsum = 0
count =0

while True:
    rannumlist = list(str(normalnum))
    for i in (0,len(rannumlist)-1):
        numsum = numsum + (int(rannumlist[i])*int(rannumlist[i]))
    if numsum == 1:
        print(orignormalsum,"is  Happy Number!")
        exit()
    else:
        normalnum = int(numsum)
        numsum =0
    count = count+1
    if count > 50000:
        print(orignormalsum,"is NOT a Happy Number!")
        exit()

