import  random

num = random.randint(10,20)
print(num,'\n')

irange = []
isum = 0
i=0
x=True
while x:
    i = i+1
    isum = isum + 2**i
    if isum >= num:
        x=False
        break
    irange = irange + [i]

print(isum)
print('\n')
print(irange)
