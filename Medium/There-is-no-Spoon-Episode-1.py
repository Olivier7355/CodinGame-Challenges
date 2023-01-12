import sys
import math

width = int(input())                    # the number of cells on the X axis
height = int(input())                   # the number of cells on the Y axis
lines = []
for i in range(height):
    line = input()                 
    lines.append(list(line))            # Create a 2d list

for y in range(height):                 # Iterate trough each line
    for x in range(width):              # Iterate trough each coloumn
        if lines[y][x]==".":
            continue                    # Go back to the for loop is the point is not a node
    
        rx = ry = bx = by = -1
       
        """ Search the next node at the right """
        for tx in range(x+1,width):     # Scan form X+1 to the end of the line
            if(lines[y][tx]=='0'):
                rx = tx
                ry = y
                break                   # if found '0', stop to scan

        """ Search the next node below """
        for ty in range(y+1, height):# Scan from y+1 to the end of the coloumn
            if(lines[ty][x]=='0'):
                bx = x
                by =ty
                break                   # if found '0', stop to scan

        print("{0} {1} {2} {3} {4} {5}".format(x, y, rx, ry, bx, by))
