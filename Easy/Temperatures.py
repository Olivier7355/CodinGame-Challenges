import sys
n = int(input())

temperatureList = input().split()

if not temperatureList :
    nearest = 0
else :

    temperatureList = [int(t) for t in temperatureList]

    nearest = temperatureList[0]

    if (len(temperatureList) > 1) :
        for t in temperatureList :
            if nearest is None or abs(t) < abs(nearest) or (abs(t) == abs(nearest) and t > 0):
                nearest = t

print(nearest)
