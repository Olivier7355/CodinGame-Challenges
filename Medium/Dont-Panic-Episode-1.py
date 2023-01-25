# https://www.codingame.com/ide/puzzle/don't-panic-episode-1
import sys, math

nbFloors, width, nbRounds, exitFloor, exitPos, nbTotalClones, nbAdditionalElevators, nbElevators = [int(i) for i in input().split()]

map = [exitPos] * nbFloors

for i in range(nbElevators):
    elevatorFloor, elevatorPos = [int(i) for i in input().split()]
    map[elevatorFloor] = elevatorPos

while True:
    cloneFloor, clonePos, direction = input().split()
    cloneFloor = int(cloneFloor)
    clonePos = int(clonePos)

    if clonePos < map[cloneFloor] and direction == "LEFT" or \
       clonePos > map[cloneFloor] and direction == "RIGHT":
       print('BLOCK')
    else:
        print('WAIT')
