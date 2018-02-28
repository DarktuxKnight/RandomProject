import string
import random

pilength = random.randint(4,10)
print(pilength)

temp = 22/7
temp = str(temp)
x = temp.split('.')[0] + '.'

numx = 22
decstring = ''
tempmod = numx%7
for i in range(0,pilength):
    tempmod = int(str(tempmod) + str('0'))
    decstring = str(decstring) + str(tempmod/7).split('.')[0]
    tempmod = int(str(tempmod%7))

print(float(str(x)+str(decstring)))
