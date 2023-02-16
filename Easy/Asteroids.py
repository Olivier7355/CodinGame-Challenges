# https://www.codingame.com/ide/puzzle/asteroids
# 60% test cases passed


import sys
import math

firstPictureList = []
secondPictureList = []

w, h, t1, t2, t3 = [int(i) for i in input().split()]
for i in range(h):
    first_picture_row, second_picture_row = input().split()
    firstPictureList.append(first_picture_row)
    secondPictureList.append(second_picture_row)

thirdPictureList = []
alphabet = []
asteroidCoordinatet1 = [10000,10000]
asteroidCoordinatet2 = [10000,10000]
movex, movey = '', ''
deltax, deltay = 0, 0
t3x, t3y = 0, 0
coordinateTable ={'':0, 'North':-1, 'South':1, 'East':1, 'West':-1}

# Find all the letters that are on the map and save in a list
for row in range(h) :
    for column in range(w) :
        if (firstPictureList[row][column] != '.') and (firstPictureList[row][column] not in alphabet) : alphabet.append(firstPictureList[row][column])
         
# Start the loop from Z to A
alphabet.sort()
alphabet.reverse()
thirdPictureList = ['.'*w]*h

# For each asteroid in firstPictureList :

for letter in range(len(alphabet)) :
    
    asteroidCoordinatet1 = [10000,10000]
    asteroidCoordinatet2 = [10000,10000]
    movex, movey = '', ''
    deltax, deltay = 0, 0
    t3x, t3y = 0, 0
    
    for row in range(h) :
        for column in range(w) :
            
            # Scan map t1
            if (firstPictureList[row][column] == alphabet[letter]) and (asteroidCoordinatet1[0] == 10000) :
                asteroidCoordinatet1[0] = column
                asteroidCoordinatet1[1] = row
            
            # Scan map t2    
            if (secondPictureList[row][column] == alphabet[letter]) and (asteroidCoordinatet2[0] == 10000) :
                asteroidCoordinatet2[0] = column
                asteroidCoordinatet2[1] = row
    
    if (asteroidCoordinatet1[0] < asteroidCoordinatet2[0]) : movex = 'East'
    elif (asteroidCoordinatet1[0] > asteroidCoordinatet2[0]) : movex = 'West'
    
    if (asteroidCoordinatet1[1] < asteroidCoordinatet2[1]) : movey = 'South'
    elif (asteroidCoordinatet1[1] > asteroidCoordinatet2[1]) : movey = 'North'
        
    # Find the number of steps (delta) between t1 and t2
    deltax = abs(asteroidCoordinatet1[0] - asteroidCoordinatet2[0])
    deltay = abs(asteroidCoordinatet1[1] - asteroidCoordinatet2[1])
    deltat = t2 - t1
    
    if movex == 'East' : t3x = int((deltax / deltat) *(t3-t1))
    else : t3x = asteroidCoordinatet1[0] - int((deltax / deltat) *(t3-t1))
    #t3x = t3x%w
    
    if movey == 'South' : t3y = int((deltay / deltat) *(t3-t1))
    else : t3y = asteroidCoordinatet1[1] - int((deltay / deltat) *(t3-t1))
    t3y = t3y%h
    
    if (t3x > -1 ) and (t3x < w) :
        new_character = alphabet[letter]
        temp = list(thirdPictureList[t3y]) 
        temp[t3x] = new_character
        thirdPictureList[t3y] = "".join(temp)
        
# Print t3
for eachLine in thirdPictureList :
    print(eachLine)
