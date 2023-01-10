# https://www.codingame.com/ide/puzzle/horse-racing-duals

import sys
import math

horsesList =[]
n = int(input())
for i in range(n):
    pi = int(input())
    horsesList.append(pi)

# Sort the list of horses
horsesList.sort()

# Initialize variable
closest = horsesList[1] - horsesList[0]

# For each element in the list :
for i in range(len(horsesList)-1) :
   
    # Compare consecutive element of the list
    if horsesList[i+1] - horsesList[i] < closest :
        closest = horsesList[i+1] - horsesList[i] 

print(closest)
