import string
import random

pilength = random.randint(4,10)
#print(pilength)

temp = 22/7
temp = str(temp)
x,y = temp.split('.')
x = x + '.'

numx = 22
decstring = ''
for i in range(0,pilength):
    tempmod = numx%7
    tempmod = int(str(tempmod) + str('0'))
    print(tempmod)

    dec,other = str(tempmod/7).split('.')
    decstring = str(decstring) + str(dec)

    numx = int(str(tempmod%7) + str('0'))

print(str(x) + str(decstring))
