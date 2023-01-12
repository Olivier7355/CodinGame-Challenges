import sys
import math

light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
thorMoveX = initial_tx
thorMoveY = initial_ty

while True:

    remaining_turns = int(input())
    NSDirection =''
    WEDirection =''

    if thorMoveX < light_x :
        thorMoveX += 1
        WEDirection ='E'
    elif thorMoveX > light_x:
        thorMoveX -= 1
        WEDirection ='W'

    if thorMoveY < light_y :
        thorMoveY += 1
        NSDirection ='S'
    elif thorMoveY > light_y  :
        thorMoveY -= 1
        NSDirection ='N'  

    print(NSDirection + WEDirection)
