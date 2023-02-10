# IN PROGRES...........................


#Testcase1
#theInput = '5 5 1 2 3'
#firstPictureList = ['A....', '.....', '.....', '.....', '.....']
#secondPictureList = ['.A...', '.....', '.....', '.....', '.....']

#Testcase2
#firstPictureList = ['A....', '.....', '.....', '.....', '.....']
#secondPictureList = ['.....', 'A....', '.....', '.....', '.....']

#Testcase3
#firstPictureList = ['A....', '.....', '.....', '.....', '.....']
#secondPictureList = ['.....', '.A...', '.....', '.....', '.....']

#Testcase4 negative
#firstPictureList = ['.....', '.....', '..A..', '.....', '.....']
#secondPictureList = ['.....', '.A...', '.....', '.....', '.....']

#Testcase5
#theInput = '6 6 1 5 6'
#firstPictureList = ['A.....', '......', '......', '......', '......', '......']
#secondPictureList = ['....A.', '......', '......', '......', '......', '......']

#Testcase6
#theInput = '6 6 1 3 5'
#firstPictureList = ['A.....', '......', 'B.....', '......', '......', '......']
#secondPictureList = ['.A....', 'B.....', '......', '......', '......', '......']

#Testcase7
#theInput = '6 6 1 6 11'
#firstPictureList = ['..H...', '......', 'E...G.', '......', '..F...', '......']
#secondPictureList = ['......', '..H...', '.E.G..', '..F...', '......', '......']

#Testcase8
#theInput = '5 5 0 1255 9999'
#firstPictureList = ['.....', '.A...', '.....', '...D.', '.....']
#secondPictureList = ['.....', '.A...', '.....', '...D.', '.....']

#Testcase9
theInput = '10 10 100 200 300'
firstPictureList = ['A.........', 'B.........', 'C.........', 'D.........', 'E.........', '.........F', '.........G', '.........H', '.........I', '.........J']
secondPictureList = ['.A........', '..B.......', '...C......', '....D.....', '.....E....', '........F.', '.......G..', '......H...', '.....I....', '....J.....']


thirdPictureList = []
alphabet = []
asteroidCoordinatet1 = [10000,10000]
asteroidCoordinatet2 = [10000,10000]
movex, movey = '', ''
deltax, deltay = 0, 0
t3x, t3y = 0, 0
coordinateTable ={'':0, 'North':-1, 'South':1, 'East':1, 'West':-1}

w, h, t1, t2, t3 = [int(i) for i in theInput.split()]

# Find all the letters that are on the map and save in a list
for row in range(h-1) :
    for column in range(w-1) :
        if (firstPictureList[row][column] != '.') and (firstPictureList[row][column] not in alphabet) : alphabet.append(firstPictureList[row][column])
        
# Start the loop from Z to A
alphabet.sort()
alphabet.reverse()
print('Alphabet :',alphabet )
thirdPictureList = ['.'*w]*h

# For each asteroid in firstPictureList :

for letter in range(len(alphabet)) :
    
    asteroidCoordinatet1 = [10000,10000]
    asteroidCoordinatet2 = [10000,10000]
    movex, movey = '', ''
    deltax, deltay = 0, 0
    t3x, t3y = 0, 0
    
    for row in range(h-1) :
        for column in range(w-1) :
            
            # Scan map t1
            if (firstPictureList[row][column] == alphabet[letter]) and (asteroidCoordinatet1[0] == 10000) :
                asteroidCoordinatet1[0] = column
                asteroidCoordinatet1[1] = row
    
            
            # Scan map t2    
            if (secondPictureList[row][column] == alphabet[letter]) and (asteroidCoordinatet2[0] == 10000) :
                asteroidCoordinatet2[0] = column
                asteroidCoordinatet2[1] = row
    
    print('Letter :', alphabet[letter])
    print(asteroidCoordinatet1, asteroidCoordinatet2)
    
    
    if (asteroidCoordinatet1[0] < asteroidCoordinatet2[0]) : movex = 'East'
    elif (asteroidCoordinatet1[0] > asteroidCoordinatet2[0]) : movex = 'West'
    
    if (asteroidCoordinatet1[1] < asteroidCoordinatet2[1]) : movey = 'South'
    elif (asteroidCoordinatet1[1] > asteroidCoordinatet2[1]) : movey = 'North'
        
    # Find the number of steps (delta) between t1 and t2
    deltax = abs(asteroidCoordinatet1[0] - asteroidCoordinatet2[0])
    deltay = abs(asteroidCoordinatet1[1] - asteroidCoordinatet2[1])
    deltat = t2 - t1
    
    print('Direction :', movex, movey)
    print('Delta :', deltax, deltay)
    print('Delta t2-t1:', deltat)
    
    if movex == 'East' : t3x = int((deltax / deltat) *(t3-t1))
    else : t3x = asteroidCoordinatet1[0] - int((deltax / deltat) *(t3-t1))
    t3x = t3x%w
    
    if movey == 'South' : t3y = int((deltay / deltat) *(t3-t1))
    else : t3y = asteroidCoordinatet1[1] - int((deltay / deltat) *(t3-t1))
    t3y = t3y%h
    
    print('T3 :', t3x, t3y)
    print('T3 % :', t3x%w, t3y%h)
        
    #thirdPictureList = ['.'*w]*h
    print(thirdPictureList)
    
    new_character = alphabet[letter]
    temp = list(thirdPictureList[t3y]) 
    print(temp)
    temp[t3x] = new_character
    print(temp)
    thirdPictureList[t3y] = "".join(temp)
    print(thirdPictureList)
    print('--------------------')


# Print t3
for eachLine in thirdPictureList :
    print(eachLine)
