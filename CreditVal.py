from random import randint
import string

def randomx(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start,range_end)

creditnum = randomx(15)
origcreditnum = creditnum
#print(creditnum)

creditnum = list(str(creditnum))
lastdig = int(creditnum[-1])
#print(creditnum)
#print(lastdig)

creditnumlen = len(creditnum)

creditrevnum = []
n=creditnumlen-1
x=0
while n != -1:
    creditrevnum.append(creditnum[n])
    n = n-1
    x = x+1

creditnum = creditrevnum[1:]
#print(creditnum)

for z in range(1,len(creditnum)):
    if z%2 == 1:
        creditnum[z-1] = 2*int(creditnum[z-1])
#print(creditnum)

totalsum = 0
for item in range(0,len(creditnum)-1):
    if int(creditnum[item]) > 9:
        temp = int(creditnum[item])-9
        totalsum = totalsum + temp
    else:
        totalsum = totalsum + int(creditnum[item])
#print(totalsum)
creditmod = totalsum % 10


if creditmod == lastdig:
    print("Valid Creditcard nuber!")
    print(origcreditnum)
else:
    print("Invalid Creditcard number")
    print(origcreditnum)

print(creditmod)
print(lastdig)


