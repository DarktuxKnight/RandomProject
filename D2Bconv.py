import random

num = random.randint(100,200)
print(num,'\n')

bitarray = []

while True:
    tempq = num//2
    tempr = num%2

    if tempr == 0:
        bitarray = bitarray + [0]
    if tempr == 1:
        bitarray = bitarray + [1]

    num = tempq
    if num == 0:
        break
list(reversed(bitarray))
print(bitarray)
