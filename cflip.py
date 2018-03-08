from random import  randint

numflips = randint(20,30)
print("Tries:",numflips)

numtails = 0
numheads = 0

for i in range(0,numflips):
    getflip = randint(0,1)
    if getflip == 0:
        numtails = numtails+1
    else:
        numheads = numheads+1
print("Number of Tails:",numtails)
print("Number of Heads:",numheads)