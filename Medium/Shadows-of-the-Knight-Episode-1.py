import sys
import math

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]


batRow = y0
batCol = x0

maxX,maxY = w,h
minX,minY = 0,0

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    
    if bomb_dir :

        if 'U' in bomb_dir :
            maxY = batRow - 1

        if 'D' in bomb_dir :
            minY = batRow + 1

        if 'R' in bomb_dir :
            minX = batCol + 1
            
        if 'L' in bomb_dir :
            maxX= batCol - 1
            
        batCol = (maxX + minX) // 2
        batRow = (maxY + minY) // 2

    # the location of the next window Batman should jump to.
    print(batCol,batRow)
