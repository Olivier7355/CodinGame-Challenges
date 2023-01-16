# https://www.codingame.com/ide/puzzle/ghost-legs

import sys
import math

lineList = []

w, h = [int(i) for i in input().split()]

# Save each line in a lineList
for i in range(h):
    lineList.append(input())

# Scan lineList
for cnt in range(0,w,3) :
    indice = 0
    for i in range(1, h-1) :
        
        if ((cnt+indice) < w-3) and ((cnt+indice) > 0) :
            if (lineList[i][cnt+indice+1] == '-'): 
                indice += 3
            elif (lineList[i][cnt+indice-1] == '-') : 
                indice -= 3          
        elif ((cnt+indice) == 0) and (lineList[i][cnt+indice+1] == '-'): 
            indice += 3
        elif ((cnt+indice) == w-1) and (lineList[i][cnt+indice-1] == '-') : 
            indice -= 3
            
    print(lineList[0][cnt] + lineList[-1][cnt + indice])
