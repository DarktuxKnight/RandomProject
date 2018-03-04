import string
import random

num = random.randint(50,100)
print(num)
primearray = []
for i in range(1,num):
    if num%i == 0:
        primearray =primearray + [i]
print(primearray)
