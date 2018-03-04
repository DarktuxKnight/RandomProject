import string
import random

num = random.randint(10000000000,20000000000)
print(num)
primearray = []
for i in range(1,num):
    if num%i == 0:
        print(i)
        primearray =primearray + [i]
print(primearray)

primefac = []
print('\n')
for x in primearray:
    primarr = []
    for y in range(1,x+1):
        if x%y == 0:
            primarr = primarr + [y]
    if len(primarr) == 2:
        primefac = primefac + [x]
print(primefac)