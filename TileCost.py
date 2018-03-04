import string
import random

width = random.randint(20,50)
height = random.randint(20,50)
print(width,height)


single_tile_cost = 15
single_tile_size = [5,10]

area_of_floor = width * height
area_of_tile = 5*10


print(area_of_floor)
print(area_of_tile)

x=0
y=0
while x < area_of_floor:
    x = x+area_of_tile
    y=y+1
print(x,y)