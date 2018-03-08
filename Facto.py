from random import randint
import string

factnum = randint(5,10)
print(factnum)
itefactnum = factnum
endnum = 1
for i in range(1,factnum):
    endnum = endnum*(i+1)
print(endnum)
