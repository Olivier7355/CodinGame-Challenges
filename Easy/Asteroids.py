# IN PROGRES...........................


theInput = '5 5 1 2 3'
firstPictureList = ['A....', '.....', '.....', '.....', '.....']
secondPictureList = ['.A...', '.....', '.....', '.....', '.....']
thirdPictureList = []
asteroidCoordinatet1 = [1000,1000]
asteroidCoordinatet2 = [1000,1000]
movex, movey = '', ''
deltax, deltay = 0, 0
t3x, t3y = 0, 0
coordinateTable ={'':0, 'North':-1, 'South':1, 'East':1, 'West':-1}

w, h, t1, t2, t3 = [int(i) for i in theInput.split()]

# For each asteroid in firstPictureList :
for row in range(4) :
    for column in range(4) :
        
        # Scan map t1
        if (firstPictureList[row][column] != '.') and (asteroidCoordinatet1[0] == 1000) :
            asteroidCoordinatet1[0] = column
            asteroidCoordinatet1[1] = row
        
        # Scan map t2    
        if (secondPictureList[row][column] != '.') and (asteroidCoordinatet2[0] == 1000) :
            asteroidCoordinatet2[0] = column
            asteroidCoordinatet2[1] = row

print(asteroidCoordinatet1, asteroidCoordinatet2)

# Move East or West ?
if (asteroidCoordinatet1[1] == asteroidCoordinatet2[1]) :
    
    # Move East
    if (asteroidCoordinatet1[0] < asteroidCoordinatet2[0]) : movex = 'East'
    # Move West
    else : movex ='West'

# Move North or South ?
if (asteroidCoordinatet1[0] == asteroidCoordinatet2[0]) :
    
    # Move South
    if (asteroidCoordinatet1[1] < asteroidCoordinatet2[1]) : movey = 'South'
    # Move North
    else : movey ='North'
    
# Find the number of steps (delta) between t1 and t2
deltax = abs(asteroidCoordinatet1[0] - asteroidCoordinatet2[0])
deltay = abs(asteroidCoordinatet1[1] - asteroidCoordinatet2[1])

print('Direction :', movex, movey)
print('Delta :', deltax, deltay)

t3x = asteroidCoordinatet2[0] + (coordinateTable[movex] * deltax)
t3y = asteroidCoordinatet2[1] + (coordinateTable[movey] * deltay)
print('T3 :', t3x, t3y)
    
thirdPictureList = ['.'*w]*h

new_character = 'A'
temp = list(thirdPictureList[t3y]) 
temp[t3x] = new_character
thirdPictureList[t3y] = "".join(temp)

# Apply the delta between t2 and t3 and find the new coordinate
    
# Check if there already is an asteroid at the final coordinates
    
# Set the final coordinate if it is the closest asteroid (ord(asteroid))  

# Print t3
for eachLine in thirdPictureList :
    print(eachLine)
