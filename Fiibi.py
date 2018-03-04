import string
import random

num = random.randint(50,1000)
print(num)
fibarray = []

x = 1
y = 1
z=x+y
fibarray = fibarray +[x]
fibarray = fibarray +[y]


while z <= num :
    fibarray = fibarray + [z]
    x=y
    y=z
    z=x+y

print(fibarray)
