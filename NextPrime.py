import string
import random

num=1

while True:
    primarr = []
    for i in range(1, num + 1):
        if num % i == 0:
            primarr = primarr + [i]
    if len(primarr) == 2:
        print(num)
    num = num+1