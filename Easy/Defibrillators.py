# https://www.codingame.com/ide/puzzle/defibrillators

import sys
import math

lon = float(input().replace(',', '.'))
lat = float(input().replace(',', '.'))
n = int(input())    # Number N of defibrillators

defibralatorList =[]

for i in range(n):
    defib = input()

    # split each decription to extract : Name, Longitude (degrees), Latitude (degrees)
    defibList = defib.split(';')

    # Convert Longitude (degrees), Latitude (degrees) from string to floats
    # replace the , with a .
    # Converts Longitude (degrees), Latitude (degrees) in radians
    defibList[-1] = math.radians(float(defibList[-1].replace(',', '.')))
    defibList[-2] = math.radians(float(defibList[-2].replace(',', '.')))

    # Calculate his distance from lon and lat
    x = (defibList[-2] - math.radians(lon)) * math.cos((math.radians(lat) + defibList[-1])/2)
    y = (defibList[-1] - (math.radians(lat)))
    distance = math.sqrt(x**2 + y**2) * 6371
    defibList.append(distance)

    # Append to the defibralatorList
    defibralatorList.append(defibList )

# nearest = the first distance from defibralatorList
nearest = defibralatorList[0][-1]
answer = defibralatorList[0][1]

# For each defibrilator in defibralatorList :
for i in range(len(defibralatorList)) :

    # if distance is smallest than the one in nearest :  nearest = d and answer = adress of the defibrilator
    if defibralatorList[i][-1] < nearest :
        nearest = defibralatorList[i][-1]
        answer = defibralatorList[i][1]

print(answer)
